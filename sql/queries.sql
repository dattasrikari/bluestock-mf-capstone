-- 1. Top 5 funds by 3-year return
SELECT f.scheme_name, f.fund_house, p.return_3yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 5;

-- 2. Average NAV per month, per fund
SELECT amfi_code, strftime('%Y-%m', nav_date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- 3. Total transaction amount by state
SELECT state, SUM(amount_inr) AS total_amount, COUNT(*) AS num_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 4. Funds with expense ratio under 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- 5. Top 10 funds by AUM (latest quarter)
SELECT fund_house, aum_crore
FROM fact_aum
WHERE date = (SELECT MAX(date) FROM fact_aum)
ORDER BY aum_crore DESC
LIMIT 10;

-- 6. SIP vs Lumpsum vs Redemption split
SELECT transaction_type, COUNT(*) AS num_tx, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Average SIP amount by age group
SELECT age_group, AVG(amount_inr) AS avg_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY age_group
ORDER BY avg_amount DESC;

-- 8. Funds ranked by Sharpe ratio within each category
SELECT f.category, f.scheme_name, p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY f.category, p.sharpe_ratio DESC;

-- 9. City tier (T30 vs B30) transaction split
SELECT city_tier, COUNT(*) AS num_tx, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY city_tier;

-- 10. Funds with negative alpha (underperforming benchmark)
SELECT f.scheme_name, f.fund_house, p.alpha, p.beta
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
WHERE p.alpha < 0
ORDER BY p.alpha ASC;