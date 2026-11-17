# Chore Chart V1.0 Project Charter
Drafted By: Micah Hurzeler , 11/17/26

## Purpose / Project Justification
The purpose of this application will be to assist in task management for things like household chores. Chores can be assigned to locations throughout a home, with time intervals. Another point of this project, is for my (Micah) own practice with database programming, and web-application programming. 

## Objectives and Success Criteria
A web-app is created that has access to a SQL database, with CRUD operations for Tasks/Chores, Locations, and chore assignments. The web app will be mobile-first view, since it would be easier to work with on a phone. A chore will have a time interval, based on the date of creation or the time last completed. Once the due date hits, it will become overdue, until completed. 

## High Level Requirements
A SQL database with tables for: Chores, Locations, Location Assignemnts

A Web-App that connects to and accesses the database, that can CRUD Chores, Locations, and assign / unassign chores to Locations. 

The Web-App will be a dashboard displaying chores that need to be completed, with an overdue section. 

This project should run on a single docker container.

## Assumptions / Constraints
Web security is not a priority for V1.0 of the project. 

Database will be persistent, based on MySQL.

## Project Roles / Responsibilities
Micah Hurzeler: PM, DBA, SA, DEV, etc ... 