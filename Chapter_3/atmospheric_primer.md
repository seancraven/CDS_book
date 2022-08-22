## Radiation Modelling

This section of the book differs from the previous section as it follows a longer form example in building a model of radiation absorption. Often treatment of the greenhouse effect is incredibly simple and uses Sankey diagrams, which illustrate  the effect that increased radiation retention produces warming. However, they lack any information on the mechanisms taking place. Unfortunately, the phenomena that drive the greenhouse effect and warming are highly interdependent. This interdependency does not lend them to simple models, which produce a convincing picture of the atmosphere. This section of the book explores building a simple radiative transfer model. This excludes any longitude or latitude variation, clouds and albedo effects and simply models an average column of atmosphere. 

Before we dive into atmospheric physics, we will look into absorption spectra, as absorption is one of the fundamental mechanisms that drive the greenhouse effect.

Line spectra arise from energy level transitions within atoms. For example, a transition can occur when sufficient energy photons interact with a molecule. The coupling of the states to the EM-field governs the transition's probability. With different strength interactions provide differing intensities of line-by-line spectra, the stronger the interaction, the more likely it will occur and the increased magnitude of the absorption line. 

This section will not deal with photon-molecule interactions as photon densities in systems like these are large enough that treating the coupling of atoms to a field is accurate enough and more straightforward. 
```{note}
As an exercise, you may want to estimate the photon density per meter squared, given that the temperature of Earth is $\approx 300K$.
Hint: the plank functions units are $W/m^2$. 
```
### Electron Transitions

One of the early achievements of quantum mechanics and the Bohr model was the prediction of Hydrogen's emission lines. As a result of the electronic shell model. With the advent of the Schrodinger equation solutions to Hydrogen, which describes electron orbitals in terms of 3 quantum numbers of n, l, m the principle, angular momentum, and magnetic quantum numbers. The notation for a specific wavefunction denoting a state n, l, m 
```{math}
:label:
\Phi_{n, l, m}(\textbf{r}, t) = R_{n, l}(r)Y_{l, m}(\theta, \phi)\exp(-i E_{n, l}t/\hbar).
``` 
```{note}
Given, that the Earth's balckbody emission spectra is peaked in the infra-red, it doesn't glow in our visable spectrum, are electronic transistions with energies around $10ev$, driven by outgoing radiation, emitted by the earth? 
```
The answer, to the question above is mainly no. Rotational and vibrational mode excitations are the most prominent forms of transition driven in the atmosphere. 
### Vibrational Transition 
- [ ] qm primer of this
- [ ] Charles
### Line Shapes

Spectral lines have finite width due to the uncertainty principle and the excitations having a finite lifetime. Excited states have a defined lifetime $ 2\tau$, corresponding to the characteristic decay time for the excited state. This lifetime is given by the inverse of the Einstein-A coefficient(the rate of spontaneous emission), which is [derived](http://home.uchicago.edu/~tokmakoff/TDQMS/Notes/4.3.%20Spont%20Emission%205-19-05.pdf) from ensuring equilibrium during stimulated emission.

Now, if the lifetime of the state is decaying exponentially, the decay of state b, the excited state, is $c_b(t) = \exp(-t/ 2 OD)$. $t$ is only considered for $t > 0$. 

```{margin}
This derivation is taken from{cite:p}`qmbj` [Bransden & Joachain](https://www.abebooks.co.uk/Quantum-Mechanics-Bransden-B.H-Prentice-Hall/31165015307/bd?cm_mmc=ggl-_-UK_Shopp_Textbookstandard-_-product_id=UK9780582356917USED-_-keyword=&gclid=CjwKCAjwt7SWBhAnEiwAx8ZLasethl3WG5lF-ycCcq74SArq-uzsbxzhec94Zpl94v58wXKvQsvEdxoClEIQAvD_BwE) .
```
Considering the steady state equation of the excited state as a solution to the Schrodinger equation
```{math}
:label:
    i \hbar \frac{\partial}{\partial t}\Phi_b(\textbf{r}, t) = E_b \Phi_b(\textbf{r},t).
```
```{margin}
It is worth noting that eq.{eq}`psi` is not a Schrodinger equation. The system does not possess a real energy, and thus is not hermitian. This is due to it being in a decaying state. 
```
When the spontaneous emission is taken into account, and coupling to the field is added. The time derivative of the equation for the non-steady state $\Psi(\textbf{r},t) = \phi_b(\textbf{r},t) c_b(t)$ is 
```{math}
:label: psi
    i \hbar \frac{\partial}{\partial t}\Psi_b(\textbf{r}, t) = \left(E_b - i \frac{\hbar}{ 2\tau}\right)\Psi_b(\textbf{r},t).
```
Thus the time component is;
```{math}
:label:
\Psi_b(\textbf{r}, t) = \psi_b(\textbf{r}) \exp\left[-i\left(E_b - i\frac{\hbar}{ 2\tau}\right)/t\hbar\right]
```
Noting that this can be written as the Fourier transform of some function $a(E)$, which is a superposition of energy eigenstates;
```{math}
:label:
 \exp\left[-i\left(E_b - i\frac{\hbar}{ 2\tau}\right)/t\hbar\right] = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} a(E')\exp(-iE't/\hbar)dE'.
```
Inverting the transform solves for $a(E)$ and bounding the function such that $t > 0$.
```{math}
:label:
a(E) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\exp\left[-i\left(E_b - i\frac{\hbar}{ 2 OD}\right)/t\hbar\right]\exp(iEt/\hbar)dt.
``` 
Thus, 
```{math}
:label:
a(E) = \frac{1}{\sqrt{2\pi\hbar}}\frac{-i\hbar}{E_b - E - i\hbar/ 2 OD}.
```
Thus the PDF of finding the state in state $b$ with some energy that is equal to $E = E_a + \hbar \omega$ is
```{math}
:label: prop
|a(E)|^2 = \frac{\hbar}{2\pi}\frac{1}{(E_b - E_a - \hbar \omega)^2 + \hbar^2/4 OD^2}.
```
This then determines the intensity distribution of a transition down from $b \rightarrow a$. This is proportional to a Lorentzian distribution
```{math}
:label:
f(\omega) = \frac{\Gamma^2/(4\hbar^2)}{(\omega-\omega_{ba})^2 + \Gamma^2/(4\hbar^2)}.
```
Where $\Gamma = \hbar / \tau$ and $ \omega_{ba} = (E_b - E_a)/\hbar$. The parameter $\Gamma/\hbar$ is the full width half maximum of the distribution.

### Line Broadening: Pressure
An additional significant component increases the value of $\tau$ when collisions induce transitions with other neighbouring molecules. Broadening from collisions occurs in much the same way as spontaneous emission, as there is an associated rate of transition. With a transition rate, there is an expected lifetime of a state, and thus uncertainty induced broadening. Consequently, if any de-excitation/excitation phenomena has a rate, then it has a finite line width. The sum of the rates is calculated to evaluate a transition's total rate. 

The rate of collisions is a function of the number density of the molecules($n$), the molecule's cross-section($\sigma$), and the relative velocity($v$).
```{math}
:label:
W_c = \sigma vn.
```
The rates are summed from both the natural decay and the collisions, and their reciprocal gives $\tau$. In the HITRAN database, collision broadening is broken into self-broadening and air-broadening. Although these are both still pressure-broadening phenomena, air-broadening dominates in climate modelling. 

### Line Broadening: Doppeler
The Doppler shift due to the atom's and the photon's relative motion also increases the spectral line width. This feature becomes more significant at higher temperatures due to the Boltzmann distribution of velocities. 
```{note}
The derivation for this is also taken from [Bransden & Joachain](https://www.abebooks.co.uk/Quantum-Mechanics-Bransden-B.H-Prentice-Hall/31165015307/bd?cm_mmc=ggl-_-UK_Shopp_Textbookstandard-_-product_id=UK9780582356917USED-_-keyword=&gclid=CjwKCAjwt7SWBhAnEiwAx8ZLasethl3WG5lF-ycCcq74SArq-uzsbxzhec94Zpl94v58wXKvQsvEdxoClEIQAvD_BwE).
```
 The Doppler shift in angular frequency is 
```{math}
:label:
\omega = \omega_0\left(1 \mp \frac{v}{c}\right).
```
Where $\omega_0$ is the un-shifted angular frequency and $v, c$ are the particles and lights speed, respectively. The $+$ case corresponds to an atom travelling away from the observer. Because the intensity in a region $\delta \omega \propto \delta N$, where $N$ is number of with atoms with a given velocity given by the Boltzmann distribution
```{math}
:label:
\frac{dN}{dv} = N_0 \exp(-Mv^2/2kT).
```
The expression for the intensity as a function of $\omega$,
```{math}
:label:
\mathcal{I}(\omega) = \mathcal{I}(\omega_0) \exp\left[\frac{-Mc^2}{2kT}\left(\frac{\omega - \omega_0}{\omega_0}\right)^2\right].
```
Thus the intensity of the broadening due to the Doppler effect is of a gaussian form. In these expressions, $M, K, T$ are the atomic mass, Boltzmann's constant, and temperature in $K$, respectively.

### The Voigt Profile

Because these broadening effects do not change the amount of emitted light, their area must stay constant. Thus the combination of the profiles is a convolution of Lorentzian and Gaussian distribution functions.
```{math}
:label:
[f_l(\omega; \Gamma) * f_g(\omega;\sigma)] (\omega; \Gamma, \sigma) = \frac{Re[w(z)]}{\sigma \sqrt{2\pi}}
```
Where 
```{math}
:label: 
w(z) = \frac{\omega -\omega_0 + i\Gamma}{\sigma \sqrt{2}}
```
For the line widths $\sigma = \omega_0 \sqrt{\frac{Mc^2}{kt}}$. This expression is the voight profile, the line shape used by the rest of the book. One can, use either a Lorentzian or Doppler profile and disregard an aspect of broadening. However, evaluation of the Voight profile is not substantially more computationally expensive and contains some interesting physics so it is retained. There are further evolutions of the Voight profile, for example, the Heartmann-Tran profile{cite}`Hartmann-Tran`. 

The book's next section briefly refreshes the mechanics of black body radiation. 
