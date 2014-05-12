Detection

For each detector/station

- Arrival time
    GPS time
- Particle density
    Number of particles


Errors

- Time
    GPS error
    Shower thickness
    Travel time in detector/pmt
    Offsets

- Density
    Energie verlies (Poisson)
    Licht transport (Gauss)
    MPV
    Gammas


Simulation

- Particles
    Arrival time
    Position


Reconstruct

- Angle (Niek)
    zenith, azimuth
- Core position (Norbert)
    x, y (lon/lat)
- Primary energy (Arne)
    energy, size, kind


Procedure

- For each energy/kind/angle
- Place showers over detectors
- Change rotation and core position of shower (to reuse)
- Assume perfect detector
- Perform reconstruction
- Apply errors to detection
- Perform recontruction
- Error analysis


Data quality

- Check station uptimes
    Count up station without detection as 0
    Count down stations as missing (ignore)
- MPV fits
    Cut data without good MPV fits

