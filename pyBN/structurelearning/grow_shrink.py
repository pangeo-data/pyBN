"""
********************
GrowShrink Algorithm
********************

"Our approach constructs Bayesian networks by first identifying each node's
Markov blankets, then connecting nodes in a maximally consistent way. 
In contrast to the majority of work, which typically uses hill-climbing approaches 
that may produce dense and causally incorrect nets, our approach yields much more 
compact causal networks by heeding independenciesin the data. Compact causal networks
facilitate fast inference and are also easier to understand. We prove that under mild 
assumptions, our approach requires time polynomial in the size of the data and the number 
of nodes. A randomized variant, also presented here, yields comparable results at
much higher speeds" [1].

This algorithm relies on the "Markov Blanket", which is for a given random variable
the set of other random variables which render the given RV conditionally independent
from the rest of the network. That is, if you observe any of the variables in a given
RV's markov blanket, then observing the values of any OTHER variables in the network
will not change your beliefs about the given random variable.

The Markov blanket of a node X is easily identifiable from the graph: 
it consists of X's parents, X's children, and the parents of all of X's children.

The runtime of this algorithm is O(|V|) [1].

References
----------
[1] Margaritis and Thrun: "Bayesian Network Induction via Local Neighborhoods", 
NIPS 2000.

[2] https://www.cs.cmu.edu/~dmarg/Papers/PhD-Thesis-Margaritis.pdf

"""

__author__ = """Nicholas Cullen <ncullen.th@dartmouth.edu>"""


def gs(bn, 
		data):
	"""
	Perform growshink algorithm over dataset to learn
	Bayesian network structure.

	Arguments
	---------
	*bn* : a BayesNet object
		BayesNet object you wish to modify
	*data* : pandas dataframe or nested numpy array
		Data from which you wish to learn structure

	Returns
	-------
	*bn* : a BayesNet object

	Effects
	-------
	None

	Notes
	-----

	"""
	S = []

	grow_condition = True
	while grow_condition:
		pass



	shrink_condition = True
	while shrink_condition:
		pass
	














