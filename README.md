# Parametric Tokamak Reactor Geometry

A learning project exploring **CAD-as-code** and **differentiable geometry** for fusion reactor design, built with [build123d](https://github.com/gumyr/build123d) (OCCT-based parametric CAD) and [JAX](https://github.com/google/jax) (autodiff).

The project uses a tokamak (rather than a stellarator) as the test geometry, purely because its axisymmetry makes the CAD mechanics simpler to learn — the underlying skills (parametric solid modeling, component relationships, differentiable shape optimization) transfer directly to more complex reactor concepts.

## Motivation

Built to develop practical familiarity with the kind of pipeline used in fusion reactor engineering: **parametric description → CAD → meshing → simulation/optimization**, with an emphasis on components that relate to each other (e.g. coil-to-vessel clearance) rather than isolated parts, and on making key design quantities differentiable for gradient-based design exploration.

## What's modeled

- **Vacuum vessel** — a toroidal shell whose poloidal cross-section follows the [Miller parametrization](https://doi.org/10.1063/1.872666) (`R₀`, minor radius `a`, elongation `κ`, triangularity `δ`), with support for variable wall thickness (inboard vs. outboard).
- **Poloidal field (PF) coil** — a continuous revolved shell, offset radially outward from the vessel by a clearance gap.
- **Toroidal field (TF) coil** — a single D-shaped loop confined to one poloidal plane, built by sweeping a small conductor cross-section along the (offset) Miller boundary curve — geometrically distinct from the PF coil, matching how a real TF coil is a discrete loop rather than a continuous shell.
- **Assembly** — vessel and coils combined into one scene, with a build123d-computed minimum clearance check between components.

## Differentiable layer (`differentiable/`)

The Miller boundary curve and the vessel–coil clearance relationship are reimplemented in JAX, separately from the CAD geometry (since OCCT-based B-rep solids are not differentiable). This lets key design quantities — e.g. minimum clearance as a function of gap, elongation, or triangularity — be optimized via gradient descent, with the resulting parameters fed back into build123d to regenerate the actual CAD solid.

## Project structure

```
params.py                  # TokamakParams dataclass (epsilon, kappa, delta, alfa, thickness, ...)
miller.py                  # Miller boundary point sampling, shared by vessel and both coil types
vacum_chamber_param.py     # vacuum vessel solid (face + revolve)
PoloidalF_magnet.py        # PF coil solid (face + revolve, offset from vessel)
ToroidalF_magnet_coil.py   # TF coil solid (sweep along Miller path)
assembly.py                # combines components, runs clearance checks

Vacum Chamber variable profile function plot #plots the profile function of the wall of the vessel

NEXT: differentiable/ WORK IN PROGRESS....
  miller_jax.py             # JAX port of the Miller boundary formula
  clearance.py              # differentiable vessel-coil clearance
  optimize.py               # gradient-based parameter optimization
```

## Known simplifications

- TF coils here are planar (confined to one poloidal plane) with a constant circular cross-section; real TF coils have some out-of-plane ("saddle") curvature and often a variable/rectangular cross-section for structural and engineering reasons.
- Only a single TF coil is modeled rather than the full toroidally-arrayed set.
- No divertor, blanket, cryostat, or port structures are modeled.

## Background reading

- Miller *et al.*, "Noncircular, finite aspect ratio, local equilibrium model," *Phys. Plasmas* 5, 973 (1998).
- Cerfon & Freidberg-lineage, "Simple, general, realistic, robust, analytic tokamak equilibria," *J. Plasma Phys.* (2021).
- Luce, "A convenient analytical parametrization of a tokamak plasma last closed flux surface," *Plasma Phys. Control. Fusion* (2024).
