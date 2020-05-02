# criptoguy

## PRNG

Some definitions of a Pseudo-Random Numbers Generator:

- Deterministic algorithms
- Appear random
- Uniformly distribution
- Independent and uncorraleted real numbers in <img src="https://render.githubusercontent.com/render/math?math=[0,1)">
- Finite State Machine 

**Definition**:
 A pseudo-random number generator <img src="https://render.githubusercontent.com/render/math?math=G"> is a struture <img src="https://render.githubusercontent.com/render/math?math=(\zeta, \mu, f, \mathscr{U}, g)">, where <img src="https://render.githubusercontent.com/render/math?math=\zeta"> is a finite set of states, <img src="https://render.githubusercontent.com/render/math?math=\mu"> is the probability distribution on <img src="https://render.githubusercontent.com/render/math?math=\zeta"> for the initial state seed, <img src="https://render.githubusercontent.com/render/math?math=f:\zeta \rightarrow \zeta"> is the transition function, <img src="https://render.githubusercontent.com/render/math?math=\mathscr{U}"> is the output space and <img src="https://render.githubusercontent.com/render/math?math=g: \zeta \rightarrow \mathscr{U}"> is the output function. The generator <img src="https://render.githubusercontent.com/render/math?math=G"> generates the number in the following way.
 
 1. Select the seed <img src="https://render.githubusercontent.com/render/math?math=s_0 \in \zeta"> based on <img src="https://render.githubusercontent.com/render/math?math=\mu">. The first number is <img src="https://render.githubusercontent.com/render/math?math=u_0 = g(s_0)">.
 2. At each steo <img src="https://render.githubusercontent.com/render/math?math=i \geq 1">, the state of hte PRNG is <img src="https://render.githubusercontent.com/render/math?math=s_i = f(s_{i-1})"> and output is <img src="https://render.githubusercontent.com/render/math?math=u_i = g(s_i)">. These output <img src="https://render.githubusercontent.com/render/math?math=u_i = u_is"> of PRNG are the (pseudo-)random numbers.


## Cellular Automata 

The Elementary Cellular Automata (CA) is a set of 256 simple rules of temporal evolution, proposed by Stephen Wolfram. The Elementary CA algorithm works according to the neighborhood of each cell of a one-dimensional row, that is, the next generation row will be the result of the application of the rule by interaction of the neighbors of the previous cell. Due to this, A cell and its two neighbors form a neighborhood of 3 cells, so there are 2^3 = 8 possible patterns for a neighborhood, then, there are 2^8 = 256 possible rules.

For example, the rule 30 (or 00011110 in binary form) works as the following:

111 --> 0

110 --> 0

101 --> 0

100 --> 1

011 --> 1

010 --> 1

001 --> 1

000 --> 0
 
 These set of simple rules could behave in a very complex and apparently random way, as you can see in next animation:
 
![Alt Text](https://giphy.com/gifs/UoXrYsYYqcrealZSLH/html5)
 
 More information about Cellular Automata you can see in the book A New Kind of Science by Stephen Wolfram.
