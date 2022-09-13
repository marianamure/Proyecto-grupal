-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema weedproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema weedproject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `weedproject` DEFAULT CHARACTER SET utf8mb3 ;
USE `weedproject` ;

-- -----------------------------------------------------
-- Table `weedproject`.`buyers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`buyers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NULL DEFAULT NULL,
  `n_identification` VARCHAR(150) NULL DEFAULT NULL,
  `email` VARCHAR(150) NULL DEFAULT NULL,
  `address` VARCHAR(150) NULL DEFAULT NULL,
  `password` VARCHAR(150) NULL DEFAULT NULL,
  `type_buyer` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `weedproject`.`cultivators`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`cultivators` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NULL DEFAULT NULL,
  `n_identification` VARCHAR(150) NULL DEFAULT NULL,
  `email` VARCHAR(150) NULL DEFAULT NULL,
  `password` VARCHAR(150) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `weedproject`.`crops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`crops` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `farm` VARCHAR(45) NULL,
  `state` VARCHAR(150) NULL DEFAULT NULL,
  `municipality` VARCHAR(150) NULL DEFAULT NULL,
  `fertilizer` VARCHAR(150) NULL DEFAULT NULL,
  `f_amount` FLOAT NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `disease` VARCHAR(150) NULL DEFAULT NULL,
  `production` FLOAT NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `image` VARCHAR(255) NULL DEFAULT NULL,
  `share` TINYINT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_crops_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_crops_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `weedproject`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `crop_id` INT NOT NULL,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_crops1_idx` (`crop_id` ASC) VISIBLE,
  INDEX `fk_comments_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_crops1`
    FOREIGN KEY (`crop_id`)
    REFERENCES `weedproject`.`crops` (`id`),
  CONSTRAINT `fk_comments_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `weedproject`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `p_sale` TEXT NULL DEFAULT NULL,
  `presentation` VARCHAR(255) NULL DEFAULT NULL,
  `price` VARCHAR(45) NULL DEFAULT NULL,
  `image` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `weedproject`.`shopping`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`shopping` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name_bank` VARCHAR(150) NULL DEFAULT NULL,
  `address` VARCHAR(150) NULL DEFAULT NULL,
  `home_delivery` TINYINT NULL DEFAULT NULL,
  `method_payment` TINYINT NULL DEFAULT NULL,
  `state` VARCHAR(150) NULL DEFAULT 'pendiente',
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shopping_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_shopping_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `weedproject`.`buyers` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
