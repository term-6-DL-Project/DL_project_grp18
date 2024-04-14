def get_accuracy(outputs,target):
    correct = 0
    for output, target in zip(outputs, target):
        if output > 0.5:
          output = 1.0
        else:
          output = 0.0
        if output == target:
            correct += 1
    return correct / len(outputs)
def get_precision(outputs, target):
    correct = 0
    TP = 0
    FP = 0
    for output, target in zip(outputs, target):

      if output > 0.5:
        output = 1.0
      else:
        output = 0.0
      if output == 1 and target == 1:
        TP += 1
      elif output == 1 and target == 0:
        FP += 1
    if TP + FP == 0:
      return "NA"
    return TP/(TP+FP)
def get_recall(outputs,target):
    correct = 0
    TP = 0
    FN = 0
    for output, target in zip(outputs, target):
      if output > 0.5:
        output = 1.0
      else:
        output = 0.0
      if output == 1 and target == 1:
        TP += 1
      elif output == 0 and target == 1:
        FN += 1
    if TP + FN == 0:
      return "NA"
    return TP/(TP+FN)