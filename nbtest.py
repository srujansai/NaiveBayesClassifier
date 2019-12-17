
import json
import os
import math

test_sort = {}
pos_prob_test = {}
neg_prob_test = {}


pos_To_Neg = {}
neg_To_Pos = {}



def NBayes(model_file,testing_dir,predictions_file):

    in_file = open(model_file, "r")

    dicts = json.load(in_file)
    in_file.close()

    vocabDict = dicts[0]
    posDict = dicts[1]
    negDict = dicts[2]

    total_Pos_Terms = sum(posDict.values())

    total_Neg_Terms = sum(negDict.values())

    total_Terms = sum(vocabDict.values())


    for term in vocabDict:
        if term in posDict:
            tF_pos = posDict.get(term)
        else:
            tF_pos = 1
        if term in negDict:
            tF_neg = negDict.get(term)
        else:
            tF_neg = 1

        pratio = ((tF_pos / float (total_Pos_Terms)) / float(tF_neg / total_Neg_Terms))
        pos_Ratio = math.log10(pratio)

        nratio = ((tF_neg/float (total_Neg_Terms))/ float (tF_pos/total_Pos_Terms))
        neg_Ratio = math.log10(nratio)

        pos_To_Neg[term] = pos_Ratio
        neg_To_Pos[term] = neg_Ratio

    ofile = open('Pos2Neg_Term_ratio.txt', 'w')
    for k in sorted(pos_To_Neg, key=pos_To_Neg.get, reverse=True)[:20]:
        ofile.write(k.ljust(10) + str(pos_To_Neg[k]) + "\n")
    ofile.close()


    mfile = open('Neg2Pos_Term_ratio.txt', 'w')
    for k in sorted(neg_To_Pos, key=neg_To_Pos.get, reverse=True)[:20]:
        mfile.write(k.ljust(10) + str(neg_To_Pos[k]) + "\n")
    mfile.close()


    old_pos = math.log10(total_Pos_Terms/float(total_Terms))
    old_neg = math.log10(total_Neg_Terms/float(total_Terms))


    for name in sorted(os.listdir(testing_dir)):
        with open(testing_dir + '\\' + name) as f:
            file = f.read()

        word = file.split()

        pos_Tf = 1.0
        neg_Tf = 1.0

        posValue = 0.0
        negValue = 0.0

        for w in word:

            if w in posDict:
                pos_Tf = posDict.get(w)
                if pos_Tf == 0.0:
                    pos_Tf = 1.0

            if w in negDict:
                neg_Tf = negDict.get(w)
                if neg_Tf == 0.0:
                    neg_Tf = 1.0

            posValue += math.log10(float(pos_Tf) / float(total_Pos_Terms))
            negValue += math.log10(float(neg_Tf)/float(total_Neg_Terms))

        posValue = old_pos + posValue
        negValue = old_neg + negValue

        txt_id = str(name).split(".")[0]
        pos_prob_test[txt_id] = posValue
        neg_prob_test[txt_id] = negValue



    for txt in pos_prob_test:
        pos_R = pos_prob_test.get(txt)
        neg_R = neg_prob_test.get(txt)
        if pos_R > neg_R:
            test_sort[txt] = 1
        elif pos_R == neg_R:
            test_sort[txt] = 0.5
        else:
            test_sort[txt] = 0

    totalPosR = sum(test_sort.values())
    totalNegR = len(test_sort) - totalPosR

    percentPos = (totalPosR / len(test_sort)) * 100
    percentNeg = (totalNegR / len(test_sort)) * 100
    out_file = open(predictions_file, 'w')
    out_file.write("Text file ".ljust(14) + "Positive Prob".ljust(20) + "   " + "Negative Prob".center(20) + "\n")

    for ke in neg_prob_test:
        out_file.write(str(ke).ljust(14) + str(pos_prob_test.get(ke)).ljust(20) + "   " + str(neg_prob_test.get(ke)).center(20) + "\n")

    out_file.write("Positive Reviews % =====>" + str(percentPos) + "   " + "Negative Reviews % =====>" + str(percentNeg))
    out_file.close()


a = input('Enter the model file: ')
b = input('Enter the test directory path containing text files: ')
c = input('Enter the output file or predictions file: ')

NBayes(a, b, c)