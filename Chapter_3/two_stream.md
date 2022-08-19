# Disregarding Radiative Equilibrium

As shown previously for our applications in the lower atmosphere, using purely radiative equilibrium gives some rather non-physical results for earth, thus moving to a different regime is required. By assuming that the equilibrium is controlled by both radiation and convection, the boundary conditions between each layer are much less strict. Because of the reduction in boundary conditions further degrees of freedom are introduced into the problem. Namely what determines the radiation of each block of atmosphere if it is not in equilibrium. 

The model proposed uses the ISAs temperature profile to calculate the emission from blocks of atmosphere, and has this radiation propagating through the atmosphere. This is just a solution to the two stream equations on the previous page eq.{eq}`up,down`. Because the solutions to these equations are continuous in order to calculate them there must be some approximations made.

## Discrete Two Stream Equations

Making the atmosphere into blocks of some constant thickness has already been mentioned, this is the first step on the way to our solution. 

The goal of this model is to produce a grid of values for at some altitude and wavenumber, the outgoing spectral radiance can be obtained. If this is not evident, looking at how the GHGs effect outgoing radiation, a spectral radiance plot is required, a black body curve with optical depths applied. This has to be a function of altitude, as these curves change with the temperature and pressure as the radiation travels through more of the atmosphere. This leads to a grid of spectral radiances evaluated at different altitudes, and wavenumbers. 

## Solutions on the Grid
Each point on the grid is associated with a altitude and wavenumber $(h_i, \nu_j)$. This begs the question of what do the two stream equations look like in a discrete form with such variables. 

Firstly, what values are chosen for the grid is important, points at which the line by line data is recorded are not the same for each gas in the HITRAN database, and calculating the total spectral radiance required operations where they are evaluated at the same values. To this problem there are two clear solutions, one increase the resolution of the grid such that every line is included on the wavenumber grid, this retains all the information. Alternatively, the resolution can be reduced and, in this implementation the values of the absorption coefficient can be averaged over and then evaluated at set intervals, this has two upsides, firstly it makes the computations of the fluxes faster, and secondly it makes adding further gases much easier. However, the binning does loose information. The bins implemented in the current program are integer values of wavenumber, because this was straightforward. The center of the bins is on the integer and have width $1 cm^{-1}$.

For the altitude points because the optical depth varies largely over a wide block of atmosphere, the approximation taken is that the optical depth is that of the midpoint. In the current implementation these blocks are $1km$ wide. Now the gridded values have been identified, the solutions to the equation are just a few variable transformations away. An addition of some notation for the gridpoints, is that $h_i$ are the edges of the altitude blocks and the midpoints are denoted as $h_m_i = (h_i + h_{i+1})/2$.

The two stream equations are differential equations in terms of the optical depth. Looking at only the up stream as the solution to the down stream is very similar, With a trial solution of $I_+ = A(OD) \exp(-OD)$ 
\begin{equation}
I_+(OD, \nu) = I_+(0) exp(-OD) = \int_0^{OD}\pi B(\nu, T(\OD'))\exp(-(OD-OD'))dOD'
\end{equation}
Where A(OD) must be one at the ground as the up flux at the ground is $I_+$. In order to make this more straightforward to integrate, we use a variable change 
\begin{equation}
\mathcal{T}(h_1,h_2) = \exp(-|OD(h_1)- OD(h_2)|) 
\end{equation}
```{note}
$OD(h)$ is the optical depth of the whole atmosphere up to that altitude.
```
With this transformation the upstream equation becomes
\begin{equation}
I_+(h, \nu) = I_+(0) \mathcal{T}(h, 0) - \int_{h' = h}^0 \pi B(\nu, h)d \mathcal{T}(h, h`)
\end{equation} 
Where $ h = 0 $ is where the atmosphere meets the ground. This Expression might look analytically daunting, but the discrete transformations is actually quite straight forward. The integral becomes a sum over the $\mathcal{T}(h_m_i)$ and the plank function at that altitude and wavenumber. The up stream equation on the grid is 
\begin{equation
\I_+(h_m_i, \nu_j) = \prod_{h_m_k =0}^h_m_i \mathcal{T}(h_m_i) I_+(0) + \sum_{h_m_k= 0}^h_m_i \pi B(\nu_j, h_m_k) \mathcal{T}(h_m_k). 
\end{equation} 
Where the sum and the product run over the height midpoints and the $\mathcal{T}(h_m_i) = \exp[-(OD_{h_{i+1}} - OD_h_i)].

In the simple trans implementation the $\mathcal{T}$ is calculated slightly differently, The difference in optical depths is  
\begin{equation}
OD_{h_{i+1}} - OD_h_i \approx int_{h_i}^{h_{i+1}}n(h)dh k(\nu, h_m_i)
\end{equation}
Where $k(\nu, h_m_i)$ is the absorption coefficient evaluated at the midpoint. 
This is a good approximation as for the region in question as the pressure and temperature gradients are close to linear over a one $km$ region. 

The next section explores the way the problem of calculating optical depths for all the gases is solved using the database, as for each hitran gas there are approximately 10,000 spectral line intensities in the wavenumber region that contains outgoing longwave radiation[200 cm^{-1},4000 cm^{-1}]. 