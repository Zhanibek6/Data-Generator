DROP TABLE IF EXISTS internet_plans;
CREATE TABLE IF NOT EXISTS internet_plans(
   i_id              INTEGER  NOT NULL PRIMARY KEY IDENTITY(1,1)
  ,i_name            VARCHAR(20) NOT NULL
  ,i_bandwitdh       VARCHAR(10) NOT NULL
  ,i_expiration_date INTEGER  NOT NULL
  ,i_launch_date     INTEGER  NOT NULL
);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (1,'200Mb','200',264,173);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (2,'500Mb','500',131,54);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (3,'500Mb','500',298,96);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (4,'1000Mb','1000',459,74);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (5,'1000Mb','1000',630,37);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (6,'1000Mb','1000',669,268);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (7,'500Mb','500',276,206);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (8,'1000Mb','1000',317,64);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (9,'500Mb','500',418,175);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (10,'500Mb','500',509,291);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (11,'200Mb','200',541,210);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (12,'1000Mb','1000',516,191);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (13,'200Mb','200',688,359);
INSERT INTO internet_plans(i_id,i_name,i_bandwitdh,i_expiration_date,i_launch_date) VALUES (14,'1000Mb','1000',700,276);