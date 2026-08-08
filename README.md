# Bluestock Fintech — Mutual Fund Analytics Platform

Capstone project: an end-to-end data engineering, ETL pipeline, and analytics
platform for Indian mutual fund data, built for Bluestock Fintech.

## Project Overview
Ingests publicly available AMFI India / mfapi.in data, cleans and loads it into
a SQLite database, computes fund performance & risk metrics (Sharpe, Sortino,
Alpha, Beta), and presents insights via an interactive dashboard.

## Data Sources
- AMFI India (amfiindia.com) — NAV, AUM, folio, SIP data
- mfapi.in — live historical NAV API
- NSE/BSE — benchmark index data

## Project Structure