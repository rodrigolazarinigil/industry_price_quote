CREATE TABLE industry.component_dimension
(
	id      VARCHAR(10),
	type_id VARCHAR(10),
	type 	VARCHAR(10),
	connection_type_id 	VARCHAR(10),
	outside_shape VARCHAR(50),
	base_type VARCHAR(50),
	height_over_tube NUMERIC(8,2),
	bolt_pattern_long NUMERIC(8,2),
	bolt_pattern_wide NUMERIC(8,2),
	groove INT,
	base_diameter  NUMERIC(8,2),
	shoulder_diameter  NUMERIC(8,2),
	unique_feature INT,
	orientation INT,
	weight NUMERIC(8,5)
);

CREATE TABLE industry.tube_assembly_dimension (
    id VARCHAR(10),
    quantity INT,
    component_id VARCHAR(10)
);