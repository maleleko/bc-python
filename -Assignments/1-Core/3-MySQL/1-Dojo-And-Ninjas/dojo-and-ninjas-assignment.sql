-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo-and-ninjas-schema
-- -----------------------------------------------------
-- Dojo and Ninjas Core Assignment

-- -----------------------------------------------------
-- Schema dojo-and-ninjas-schema
--
-- Dojo and Ninjas Core Assignment
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo-and-ninjas-schema` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `dojo-and-ninjas-schema` ;

-- -----------------------------------------------------
-- Table `dojo-and-ninjas-schema`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo-and-ninjas-schema`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojo-and-ninjas-schema`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo-and-ninjas-schema`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` CHAR(15) NULL,
  `last_name` CHAR(15) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojo_id` INT NOT NULL,
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojo-and-ninjas-schema`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
