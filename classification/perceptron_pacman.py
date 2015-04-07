# perceptron_pacman.py
# --------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation for apprenticeship learning
import util
from perceptron import PerceptronClassifier
from pacman import GameState

PRINT = True


class PerceptronClassifierPacman(PerceptronClassifier):
    def __init__(self, legalLabels, maxIterations):
        PerceptronClassifier.__init__(self, legalLabels, maxIterations)
        self.weights = util.Counter()

    def classify(self, data ):
        """
        Data contains a list of (datum, legal moves)
        
        Datum is a Counter representing the features of each GameState.
        legalMoves is a list of legal moves for that GameState.
        """
        guesses = []
        for datum, legalMoves in data:
            vectors = util.Counter()
            for l in legalMoves:
                vectors[l] = self.weights * datum[l] #changed from datum to datum[l]
            guesses.append(vectors.argMax())
        return guesses


    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        self.features = trainingData[0][0]['Stop'].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

        feature = self.features[0]
        
        def f(s,a):
            return s[0][a][feature]

        def score(s,a):
            sc = 0
            for i in range(len(self.features)):
                sc += self.weights[self.features[i]] * f(s,a)
            return sc
        
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            
            for i in range(len(trainingData)):
                
                "*** YOUR CODE HERE ***"
                
                state = trainingData[i]
                action = trainingLabels[i]
                actions = state[1]
                
                action1 = actions[0]
                highScore = score(state, action1)
                
                for j in range(len(actions)):
                    action2 = actions[j]
                    sc = score(state, action2)
                    if (sc > highScore):
                        action1 = action2
                        highScore = sc
                
                if (action != action1):
                    self.weights[feature] += f(state, action)
                    self.weights[feature] -= f(state, action1)

