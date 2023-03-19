from transformers import pipeline
def classipy(text):
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") 
        sequence_to_classify = text
        candidate_labels = ['form', 'invoice']
        result = classifier(sequence_to_classify, candidate_labels)
        index = 0
        for i in range(0,len(range["scores"])):
                if(range["scores"][i] > range["scores"][i+1]):
                        index = i
                else:
                        continue
        return range["labels"][i]

print(classipy("LOREM IPSUM DOLOR Reg. No. Date of Issue: / / ADMISSION FORM 0 Photo Here Surname:   Name.   Father's Name-Mother's Name. Aadhar Card No.: Date of Birth: Gender: I Male II Female Phone.   Place of Birth-City:   Dist   State.   Physical problems/Disability (if any)•   Name of School:   1 1 1 1 1 1 1 1 1 1 1 1 1 I I I I I I I I I Format (DD/MM/YY) e.g. 07/12/2000UNDERTAKING  Lorem ipsum dolor sit amet: A. Consectetur odipiscing elit.Morbi rhoncus, lorem interclum porto consequot, est mogno luctus diam, quis semperjusto mauris at mews. 8. Donec convallis accumsan mattis. Praesent ternpus ante eget diam iaculis, id posuere enim tempus. Sed fringilla eleifend odio, in finibus leo pulvinar eget C. Cros vel lorem locinio, dopibus lorem sediscelerisque oc. Signature:   VectorStock VectorStock.com/31097395"))