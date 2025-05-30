def test_predict_structure():
    from ai_modules.demand_forecasting import DemandForecaster
    import pandas as pd
    df = pd.DataFrame({'hour': list(range(24))})
    result = DemandForecaster().predict(df)
    assert 'predicted_users' in result.columns
    assert len(result) == 24