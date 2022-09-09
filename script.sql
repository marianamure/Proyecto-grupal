-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cultivos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cultivos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cultivos` DEFAULT CHARACTER SET utf8 ;
USE `cultivos` ;

-- -----------------------------------------------------
-- Table `cultivos`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(255) NULL,
  `identification` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `address` VARCHAR(150) NULL,
  `password` VARCHAR(150) NULL,
  `type_buyer` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `type_user` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cultivos`.`crops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`crops` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `farm` VARCHAR(155) NULL,
  `estate` VARCHAR(150) NULL,
  `municipality` VARCHAR(150) NULL,
  `fertilizer` VARCHAR(150) NULL,
  `f_amount` FLOAT NULL,
  `date` DATE NULL,
  `disease` VARCHAR(150) NULL,
  `product` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `image` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_crops_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_crops_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `cultivos`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cultivos`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `crop_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_crops1_idx` (`crop_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `cultivos`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_crops1`
    FOREIGN KEY (`crop_id`)
    REFERENCES `cultivos`.`crops` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cultivos`.`shoppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`shoppings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name_bank` VARCHAR(150) NULL,
  `address` VARCHAR(150) NULL,
  `get_product` TINYINT NULL,
  `method_payment` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shoppings_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_shoppings_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `cultivos`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cultivos`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `description` TEXT NULL,
  `p_sale` TEXT NULL,
  `presentation` VARCHAR(255) NULL,
  `price` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cultivos`.`shopping_cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cultivos`.`shopping_cart` (
  `product_id` INT NOT NULL,
  `shopping_id` INT NOT NULL,
  PRIMARY KEY (`shopping_id`, `product_id`),
  INDEX `fk_products_has_shoppings_shoppings1_idx` (`shopping_id` ASC) VISIBLE,
  INDEX `fk_products_has_shoppings_products1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_has_shoppings_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `cultivos`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_shoppings_shoppings1`
    FOREIGN KEY (`shopping_id`)
    REFERENCES `cultivos`.`shoppings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
