from datetime import datetime
from models.llm_analyzer import LLMAnalyzer
from models.rl_trader import RLTrader
from data.market_data import MarketData

def main():
    # Initialize components
    llm = LLMAnalyzer()
    market_data = MarketData()
    
    # Example usage
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    symbol = "AAPL"  # Example stock symbol
    
    # Fetch historical data
    prices, dates = market_data.fetch_historical_data(symbol, start_date, end_date)
    returns = market_data.preprocess_data(prices)
    
    # Example external factor analysis
    example_texts = {
        'political': "Recent policy changes affect tech sector",
        'economic': "Federal Reserve announces interest rate decision",
        'social': "Consumer sentiment shows positive trend",
        'technological': "New breakthrough in AI technology",
        'environmental': "Companies pledge carbon neutrality",
        'competitive': "New market entrant disrupts industry"
    }
    
    # Get factor scores from LLM analysis
    factor_scores = llm.get_factor_score(example_texts)
    
    # Initialize RL trader with combined state size
    state_size = len(factor_scores) + 10  # Technical indicators + factor scores
    action_size = 3  # Buy, Hold, Sell
    trader = RLTrader(state_size, action_size)
    
    print("System initialized and ready for training")

if __name__ == "__main__":
    main()