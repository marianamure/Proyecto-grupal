-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema weedproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema weedproject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `weedproject` DEFAULT CHARACTER SET utf8 ;
USE `weedproject` ;

-- -----------------------------------------------------
-- Table `weedproject`.`buyers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`buyers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NULL,
  `n_identification` VARCHAR(150) NULL,
  `emai` VARCHAR(150) NULL,
  `address` VARCHAR(150) NULL,
  `password` VARCHAR(150) NULL,
  `type_buyer` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`cultivators`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`cultivators` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NULL,
  `n_identification` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`crops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`crops` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `estate` VARCHAR(150) NULL,
  `municipality` VARCHAR(150) NULL,
  `fertilizer` VARCHAR(150) NULL,
  `f_amount` VARCHAR(45) NULL,
  `date` DATE NULL,
  `disease` VARCHAR(150) NULL,
  `product` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `image` VARCHAR(255) NULL,
  `share` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_crops_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_crops_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `description` TEXT NULL,
  `p_sale` TEXT NULL,
  `presentation` VARCHAR(255) NULL,
  `price` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`comments` (
  `id` INT NOT NULL,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `crop_id` INT NOT NULL,
  `cultivators_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_crops1_idx` (`crop_id` ASC) VISIBLE,
  INDEX `fk_comments_cultivators1_idx` (`cultivators_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_crops1`
    FOREIGN KEY (`crop_id`)
    REFERENCES `weedproject`.`crops` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_cultivators1`
    FOREIGN KEY (`cultivators_id`)
    REFERENCES `weedproject`.`cultivators` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`shopping`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`shopping` (
  `id` INT NOT NULL,
  `name_bank` VARCHAR(150) NULL,
  `address` VARCHAR(150) NULL,
  `home_delivery` TINYINT NULL,
  `method_payment` TINYINT NULL,
  `state` VARCHAR(150) NULL DEFAULT 'pendiente',
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shopping_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_shopping_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `weedproject`.`buyers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weedproject`.`shopping_cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weedproject`.`shopping_cart` (
  `product_id` INT NOT NULL,
  `shopping_id` INT NOT NULL,
  `amount` INT NULL,
  PRIMARY KEY (`product_id`, `shopping_id`),
  INDEX `fk_products_has_shopping_shopping1_idx` (`shopping_id` ASC) VISIBLE,
  INDEX `fk_products_has_shopping_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_shopping_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `weedproject`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_shopping_shopping1`
    FOREIGN KEY (`shopping_id`)
    REFERENCES `weedproject`.`shopping` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
