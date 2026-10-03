# Global Temperature Anomaly Forecast Based on CO2 Concentration

## Task
- Investigate the relationship between atmospheric CO2 concentration and global temperature anomaly
- Build and compare several prediction models
- Use the best-performing model to forecast the global temperature anomaly for the next 10 years

## Data
- Temperature anomaly: NASA GISTEMP (data.giss.nasa.gov)
- CO2 concentration: NOAA Mauna Loa Observatory (gml.noaa.gov)

## Project Structure
- `src/collect_data.py` — data collection and merging
- `notebooks/01_explore.ipynb` — EDA, model training, and visualization
- `data/raw/` — saved data and plots

## Results

| Model | MAE | RMSE |
|---|---|---|
| Linear Regression | 0.110 | 0.133 |
| Random Forest | 0.247 | 0.302 |
| Gradient Boosting | 0.231 | 0.281 |

## Conclusions
Linear Regression showed the lowest error (MAE 0.11°C compared to 0.23–0.25°C
for the ensemble models). This can be explained by two factors: first, the
relationship between CO2 concentration and temperature anomaly is close to
linear over the range considered; second, the test period (2011–2024)
contains CO2 values that extend beyond the range observed by the models
during training - tree-based models generally perform poorly when
extrapolating beyond the training range, unlike Linear Regression.

## Forecast Limitations
The forecast assumes that CO2 concentrations will continue to increase at
the rate observed over the most recent 15 years of historical data.
Real-world dynamics depend on factors not included in the model (climate
policy, changes in the energy sector, etc.), so the forecast should be
interpreted as a continuation of the current trend rather than a prediction
that accounts for possible future scenarios.

## How to Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/collect_data.py
jupyter notebook notebooks/01_explore.ipynb
```
