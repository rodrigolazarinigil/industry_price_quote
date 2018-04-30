CREATE TABLE industry.component_dimension
(
	id      VARCHAR(10) NOT NULL,
	type_id VARCHAR(10) NOT NULL,
	type 	VARCHAR(10) NOT NULL,
	connection_type_id 	VARCHAR(10) NOT NULL,
	outside_shape VARCHAR(50) NOT NULL,
	base_type VARCHAR(50) NOT NULL,
	height_over_tube NUMERIC(8,2) NOT NULL,
	bolt_pattern_long NUMERIC(8,2) NOT NULL,
	bolt_pattern_wide NUMERIC(8,2) NOT NULL,
	groove INT NOT NULL,
	base_diameter  NUMERIC(8,2) NOT NULL,
	shoulder_diameter  NUMERIC(8,2) NOT NULL,
	unique_feature INT NOT NULL,
	orientation INT NOT NULL,
	weight NUMERIC(8,5) NOT NULL,
	CONSTRAINT pk_component_dimension PRIMARY KEY (id)
);

CREATE TABLE industry.tube_assembly_dimension (
    id VARCHAR(10) NOT NULL,
    quantity INT NOT NULL,
    component_id VARCHAR(10) NOT NULL,
    CONSTRAINT pk_tube_assembly_dimension PRIMARY KEY (id),
    CONSTRAINT fk_tube_assembly_dimension FOREIGN KEY (component_id) REFERENCES industry.component_dimension (id)
);

CREATE TABLE industry.price_quote_fact (
	sk_price_quote_fact SERIAL NOT NULL,
	tube_assembly_id VARCHAR(10) NOT NULL,
	supplier VARCHAR(10) NOT NULL,
	quote_date DATE NOT NULL,
	annual_usage INT NOT NULL,
	min_order_quantity INT NOT NULL,
	bracket_pricing INT NOT NULL,
	quantity INT NOT NULL,
	cost NUMERIC(8,2) NOT NULL,
	CONSTRAINT pk_price_quote_fact PRIMARY KEY (sk_price_quote_fact),
	CONSTRAINT fk_price_quote_fact_assembly FOREIGN KEY (tube_assembly_id) REFERENCES industry.tube_assembly_dimension (id)
);