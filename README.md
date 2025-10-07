# E-commerce, Multivitamin Sales

## Project Overview
Developed a weekly sales reporting system for health supplement products, analyzing sales performance by product category, sales branch location, and discount impact. The insights support the Sales and Marketing divisions in evaluating branch performance, distribution platform efficiency, and underperforming product segments to refine sales and distribution strategies.

## Target Audience
- Sales and Marketing Departments

## Deliverables
- Data analysis and visualization through plots for further evaluation.
- Weekly sales insights by supplement category, sales branch, and discount effectiveness.

## Teknologi dan Library yang Digunakan
- **Docker**: Integrated environment running Elasticsearch, Airflow, and Kibana.
- **Database**: PostgreSQL for data storage and initial table creation.
- **Library Python**:
  - `pandas`, `datetime`, `timedelta` Time series data manipulation and management.
  - `sqlalchemy` dan `psycopg2` Database connectivity and operations with PostgreSQL.
  - `airflow` dan `PythonOperator` Workflow automation and pipeline orchestration.
  - `elasticsearch` dan `helpers` Data indexing and search capabilities.
- **Visualisasi**: Kibana for interactive, real-time data dashboards.

## Key Findings
- **Revenue by Country**:  
  - Canada leads with revenue ~$31.4M and average discount 12.5%.
  - UK follows with ~$30.8M at 12.4% average discount.
  - USA records the lowest revenue (~$29.4M) despite a similar average discount (12.5%).
- **Impact of COVID-19**:  
  - Sales of Vitamins (+30–40%) and Sleep Aids (+25%) surged during the pandemic due to increased health awareness and sleep disruption.
  - Sales of Performance and Protein segments declined during lockdowns.
  - Post-pandemic, most segments normalized, though Sleep Aids remain above pre-pandemic levels.
- **Discount Analysis**  
  Discounts remained stable across countries and are not a primary driver of revenue; unit volume and pricing have a greater impact.
- **Strategic Recommendations**  
  - Implement new market strategies for the USA to tap into its high-potential market.
  - Re-evaluate distribution and promotional efforts for stagnant or declining products (e.g., Fat Burner, Amino Acid).
  - Test bundled promotions (e.g., Protein + Hydration, Omega + Herbal) to boost cross-selling.

## Usage Instructions
1. Launch the integrated system using Docker (Elasticsearch, Airflow, Kibana).
2. Set up a PostgreSQL database and create the required data tables.
3. Run Python ETL scripts to extract, transform, and load data into PostgreSQL and Elasticsearch.
4. Execute Airflow DAGs to automate pipeline processing and refresh Kibana dashboards.
5. Access the Kibana dashboard for real-time visualizations and sales analytics.
