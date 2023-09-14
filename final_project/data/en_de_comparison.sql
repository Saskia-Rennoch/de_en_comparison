DROP DATABASE IF EXISTS en_de_comparison;
CREATE DATABASE en_de_comparison;

\c en_de_comparison

DROP TABLE IF EXISTS categories CASCADE;


--german table
DROP TABLE IF EXISTS de_degree_field_title_uni_city;
CREATE TABLE de_degree_field_title_uni_city (
    Degree VARCHAR (100),
	Field VARCHAR (200),
	Study_program TEXT,
	University TEXT,
	City TEXT);
	
\copy de_degree_field_title_uni_city FROM './de_degree_field_title_uni_city.csv' DELIMITER ';' CSV HEADER
	
--german table University;County;Tuition_fee
DROP TABLE IF EXISTS de_uni_county_fee;
CREATE TABLE de_uni_county_fee (
    University TEXT,
	County TEXT,
	Tuition_fee NUMERIC);
	
--region;university;rent_monthly_pounds;rent_year_pounds;approx_tuition_fee_yr
\copy de_uni_county_fee FROM './de_uni_county_fee.csv' DELIMITER ';' CSV HEADER
	
	
--german table
DROP TABLE IF EXISTS de_city_rent_month_rent_yr;
CREATE TABLE de_city_rent_month_rent_yr (
    City TEXT,
	Rent_monthly_pounds NUMERIC,
	Rent_yearly_pounds NUMERIC);
	

\copy de_city_rent_month_rent_yr FROM './de_city_rent_month_rent_yr.csv' DELIMITER ';' CSV HEADER

-- English part of programme
DROP TABLE IF EXISTS en_programmes;
CREATE TABLE en_programmes (
    university TEXT,
	study_programme TEXT);
	

\copy en_programmes FROM './en_programmes.csv' DELIMITER ';' CSV HEADER

DROP TABLE IF EXISTS en_reg_uni_rent_m_yr_fee;
CREATE TABLE en_reg_uni_rent_m_yr_fee (
    region TEXT,
	university TEXT,
	rent_monthly_pounds NUMERIC,
	rent_year_pounds NUMERIC,
	approx_tuition_fee_yr NUMERIC);
	
--region;university;rent_monthly_pounds;rent_year_pounds;approx_tuition_fee_yr
\copy en_reg_uni_rent_m_yr_fee FROM './en_reg_uni_rent_m_yr_fee.csv' DELIMITER ';' CSV HEADER

