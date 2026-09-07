CREATE DATABASE personal_portfolio
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE personal_portfolio;

CREATE TABLE skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(1000) NOT NULL,
    image VARCHAR(500) NULL,
    demo_url VARCHAR(500) NULL,
    github_url VARCHAR(500) NULL
);

CREATE TABLE project_skills (
    project_id INT NOT NULL,
    skill_id INT NOT NULL,

    PRIMARY KEY (project_id, skill_id),

    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE languages (
    language_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    level TINYINT NOT NULL CHECK (level BETWEEN 0 AND 100)
);

CREATE TABLE education (
    education_id INT AUTO_INCREMENT PRIMARY KEY,
    degree VARCHAR(200) NOT NULL,
    university_name VARCHAR(100) NOT NULL,
    start_at DATE NOT NULL,
    end_at DATE NULL,
    image VARCHAR(500) NULL,
    content VARCHAR(500) NULL
);

CREATE TABLE experience (
    experience_id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(100) NOT NULL,
    company_name VARCHAR(200) NOT NULL,
    start_at DATE NOT NULL,
    end_at DATE NULL
);