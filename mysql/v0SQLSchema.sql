CREATE TABLE `chores`(
    `chore_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `time_interval` BIGINT NOT NULL
);
CREATE TABLE `locations`(
    `location_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL
);
CREATE TABLE `assigned_chores`(
    `assignment_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `chore_id` BIGINT UNSIGNED NOT NULL,
    `location_id` BIGINT UNSIGNED NOT NULL,
    `is_complete` BOOLEAN NOT NULL,
    `due_date` DATETIME NOT NULL
);
ALTER TABLE
    `assigned_chores` ADD CONSTRAINT `assigned_chores_chore_id_foreign` FOREIGN KEY(`chore_id`) REFERENCES `chores`(`chore_id`);
ALTER TABLE
    `assigned_chores` ADD CONSTRAINT `assigned_chores_location_id_foreign` FOREIGN KEY(`location_id`) REFERENCES `locations`(`location_id`);