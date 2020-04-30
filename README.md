# criptoguy

## PRNG

- Deterministic algorithms
- Appear random
- Uniformly distribution
- Independent and uncorraleted real numbers in $[0,1)$
- Finite State Machine 

*Definition*:
 A pseudo-random number generator $G$ is a struture $(\zeta, \mu, f, \mathscr{U}, g)$, where $\zeta$ is a finite set of states, $\mu$ is the probability distribution on $\zeta$ for the initial state seed, $f:\zeta \rightarrow \zeta$ is the transition function, $\mathscr{U}$ is the output space and $g: \zeta \rightarrow \mathsrc{U}$ is the output function. The generator G generates the number in the following way.
 
 1. Select the seed $s_0 \in \zeta$ based on $\mu$. The first number is $u_0 = g(s_0)$.
 2. At each steo $i \geq 1$, the state of hte PRNG is $s_i = f(s_{i-1]$ and output is $u_i = g(s_i)$. These output $u_is$ of PRNG are the (pseudo-)random numbers.
 
 
