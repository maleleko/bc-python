-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books-schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema books-schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books-schema` DEFAULT CHARACTER SET utf8 ;
USE `books-schema` ;

-- -----------------------------------------------------
-- Table `books-schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books-schema`.`users` (
  `id` INT NOT NULL,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books-schema`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books-schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books-schema`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books-schema`.`favorites` (
  `book_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `user_id`),
  INDEX `fk_books_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_books_has_users_books_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_has_users_books`
    FOREIGN KEY (`book_id`)
    REFERENCES `books-schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_books_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `books-schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
