# International Geomagnetic Reference Field (IGRF)

This README requires a [MathJax](https://www.mathjax.org/) browser plugin for the mathematicsto be rendered in between then `$...$`. Many are widely available for all the major browsers.

## Magnetic Field Models

The Pherical Harmonic model presents some computational aspects of the geomagnetic field models. The Earth's magnetic field (**B**), can be represented as the gradient of a scalar potential fuction (V), i.e.,

$$B = -\nabla V$$

V can be represented by a series of spherical harmonics,

$$V(R,\theta, \phi) = a \sum_{n = 1}^{k}(\frac{a}{r})^{(n-1)}\sum_{m = 0}^{k}(g^n_mcos(m\phi)+h^n_msin(m\phi))P^m_n(\theta)$$

Where **a** is the Earth's equatorial radius (6371.2 km), $g^m_n$ and $h^m_n$ are Gaussian coefficients, and R, $\theta$, $\phi$ are geodetic coefficients describing location on Earth. 

The Gaussian coefficients are determined empirically by a least-squares fit to measurements of the field. A set of these coefficients constitutes a model of the field. The International Association of Geomagnetism and Aeronomy (IAGA) releases the Generation International Geomagnetic Reference Field every 5 years and can be used for the next 5 years.

The Legendre fuctions ($P^m_n$) is related to the Schmidt functions ($S_{n,m}$) and the Gauss function ($P^{n,m}$) as follow,

$$P^m_n = S_{n,m}P^{n,m}$$

The Schimdt factors are best combined with the Gaussian coefficients because they are independent of R, $\theta$, $\phi$ and must be calculated only once during a computer run. Thus, we define

$$ g^{n,m} = S_{n,m}  g^m_n$$
$$ h^{n,m} = S_{n,m}  h^m_n$$

The following recursion relation can be used to calculate the Schimdt factors ($S_{n,m}$):
$$S_{0,0} = 1$$
$$ S_{n,0} = S_{n-1,0}[\frac{2n-1}{n}]\quad\quad n\geq 1$$
$$S_{n,m} = S_{n,m-1} \sqrt{\frac{(n-m+1)(\delta^1_m+1)}{n+m}} \quad\quad m\geq1$$

where the Kronecker delta, $\delta^i_j =1$ is $i = j$ and 0 otherwise.

The $P^{n,m}$ can be similarly obtained from the following recursion relations:

$$P^{0,0} = 1$$
$$P^{n,n} = sin(\theta)P^{n-1,n-1}$$
$$P^{n,m} = cos(\theta)P^{n-1,m} - K^{n,m}P^{n-2,m}$$

where

$$K^{n,m} = \frac{(n-1)^2- m^2}{(2n-1)+(2n-3)} $$
$$K^{n,m} = 0$$

The gradient in the magnetic field equation leads to partial derivatives of the $P^{n, m}$. We need

$$\frac{\partial P^{0,0}}{\partial \theta} = 0$$
$$\frac{\partial P^{n,n}}{\partial \theta} = sin(\theta)\frac{\partial P^{n-1,n-1}}{\partial \theta} + cos(\theta)P^{n-1,n-1} \qquad n\geq 1$$
$$\frac{\partial P^{n,m}}{\partial \theta} = cos(\theta)\frac{\partial P^{n-1,m}}{\partial \theta}-sin(\theta)P^{n-1,m}-K^{n,m}\frac{\partial P^{n-2,m}}{\partial \theta}$$

We can calculate the magnetic field (**B**) from the gradient of $V$ using the coefficients $g^{n, m}$ and $h^{n, m}$, and the recursion relation. Specifically,

$$B_r = \frac{-\partial V}{\partial r} = \sum_{n = 1}^{k}(\frac{a}{r})^{(n+2)}(n+1)\sum_{m =0}^{n}(g^{n,m}cos(m\phi)+h^{n,m}sin(m\phi))P^{n,m}(\theta)$$
$$B_\theta = \frac{-1}{r}\frac{\partial V}{\partial \theta} = - \sum_{n=1}^{k}(\frac{a}{r})^{(n+2)}\sum_{m=0}^{n}(g^{n,m}cos(m\phi)+h^{n,m}sin(m\phi))\frac{\partial P^{n,m}(\theta)}{\partial \theta}$$
$$B_\phi =\frac{-1}{r sin(\theta)}\frac{\partial V}{\partial \theta} = \frac{-1}{sin(\theta)} \sum_{n=1}^{k}(\frac{a}{r})^{(n+2)}\sum_{m=0}^{n}(-g^{n,m}cos(m\phi)+h^{n,m}sin(m\phi)) P^{n,m}(\theta) $$