# criptoguy

## PRNG

Some definitions of a Pseudo-Random Numbers Generator:

- Deterministic algorithms
- Appear random
- Uniformly distribution
- Independent and uncorraleted real numbers in <img src="https://render.githubusercontent.com/render/math?math=[0,1)">
- Finite State Machine 

**Definition**:
 A pseudo-random number generator <img src="https://render.githubusercontent.com/render/math?math=G"> is a struture <img src="https://render.githubusercontent.com/render/math?math=(\zeta, \mu, f, \mathscr{U}, g)">, where <img src="https://render.githubusercontent.com/render/math?math=\zeta"> is a finite set of states, <img src="https://render.githubusercontent.com/render/math?math=\mu"> is the probability distribution on <img src="https://render.githubusercontent.com/render/math?math=[0,1)">$\zeta$ for the initial state seed, <img src="https://render.githubusercontent.com/render/math?math=f:\zeta \rightarrow \zeta"> is the transition function, <img src="https://render.githubusercontent.com/render/math?math=\mathscr{U}"> is the output space and <img src="https://render.githubusercontent.com/render/math?math=g: \zeta \rightarrow \mathsrc{U}"> is the output function. The generator <img src="https://render.githubusercontent.com/render/math?math=G"> generates the number in the following way.
 
 1. Select the seed <img src="https://render.githubusercontent.com/render/math?math=s_0 \in \zeta"> based on <img src="https://render.githubusercontent.com/render/math?math=\mu">. The first number is <img src="https://render.githubusercontent.com/render/math?math=u_0 = g(s_0)">.
 2. At each steo <img src="https://render.githubusercontent.com/render/math?math=i \geq 1">, the state of hte PRNG is <img src="https://render.githubusercontent.com/render/math?math=s_i = f(s_{i-1]"> and output is <img src="https://render.githubusercontent.com/render/math?math=u_i = g(s_i)">. These output <img src="https://render.githubusercontent.com/render/math?math=u_i = u_is"> of PRNG are the (pseudo-)random numbers.

