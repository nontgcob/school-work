-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Who is the theft?
-- Output the descriptions and select the one that makes the most sense.
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";
-- +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- |                                                                                                       description                                                                                                        |
-- +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- | Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
-- +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--Go through the transcripts of the interviews.
SELECT name, transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";
-- +---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- |  name   |                                                                                                                                                     transcript                                                                                                                                                      |
-- +---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
-- | Emma    | I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour. They never bought anything.                                                                                                                                                                                 |
-- +---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-- List the names of all the people who were exiting the bakery parking lot on 28th of July 2021 between 10:05-10:25 am.
SELECT name FROM people AS ppl
JOIN bakery_security_logs AS bsl ON bsl.license_plate = ppl.license_plate
WHERE bsl.year = 2021 AND bsl.month = 7 AND bsl.day = 28 AND bsl.hour = 10 AND 5 < bsl.minute < 25 AND bsl.activity = "exit";
-- +---------+
-- |  name   |
-- +---------+
-- | Vanessa |
-- | Bruce   |
-- | Barry   |
-- | Luca    |
-- | Sofia   |
-- | Iman    |
-- | Diana   |
-- | Kelsey  |
-- | Taylor  |
-- +---------+

-- List the names of all the passengers(aka the people) that was onboard the earliest flight on 29th of July 2021 departured from all of the airports in Fiftyville. (It turns out that there's only one airport in Fiftyville)
SELECT name FROM people AS ppl
JOIN passengers AS psg ON psg.passport_number = ppl.passport_number
WHERE psg.flight_id = (
    SELECT id FROM flights AS flt
    WHERE flt.year = 2021 AND flt.month = 7 AND flt.day = 29 AND flt.origin_airport_id = (
        SELECT id FROM airports
        WHERE airports.city = "Fiftyville"
    )
    ORDER BY flt.hour, flt.minute
    LIMIT 1
);
-- +--------+
-- |  name  |
-- +--------+
-- | Doris  |
-- | Sofia  |
-- | Bruce  |
-- | Edward |
-- | Kelsey |
-- | Taylor |
-- | Kenny  |
-- | Luca   |
-- +--------+

-- List the names of all the people who were withdrawing their money at Leggett Street on 28th of July 2021 before noon(12pm).
SELECT name FROM people AS ppl
JOIN bank_accounts AS bank ON bank.person_id = ppl.id
JOIN atm_transactions AS atm ON atm.account_number = bank.account_number
WHERE atm.year = 2021 AND atm.month = 7 AND atm.day = 28 AND atm.atm_location LIKE "%leggett street%" AND atm.transaction_type = "withdraw";
-- +---------+
-- |  name   |
-- +---------+
-- | Bruce   |
-- | Diana   |
-- | Brooke  |
-- | Kenny   |
-- | Iman    |
-- | Luca    |
-- | Taylor  |
-- | Benista |
-- +---------+

-- List the names of all the people who made a call less than 1 minute on 28th of July 2021.
SELECT name FROM people AS ppl
JOIN phone_calls AS call ON call.caller = ppl.phone_number
WHERE call.year = 2021 AND call.month = 7 AND call.day = 28 AND call.duration < 60;
-- +---------+
-- |  name   |
-- +---------+
-- | Sofia   |
-- | Kelsey  |
-- | Bruce   |
-- | Kelsey  |
-- | Taylor  |
-- | Diana   |
-- | Carina  |
-- | Kenny   |
-- | Benista |
-- +---------+
-- ########################################################################################################################################################################################################

-- Conclusion: Bruce is presented in all of the evidence I could find. With that said, I would conclude that Bruce is the theft that we have been looking for.

-- ########################################################################################################################################################################################################


-- Find which city the theft escaped to.
-- Which city is the destination of the flight that the theft was onboard?
SELECT city FROM airports
JOIN flights AS flt ON flt.destination_airport_id = airports.id
WHERE flt.year = 2021 AND flt.month = 7 AND flt.day = 29 AND flt.origin_airport_id = (
    SELECT id FROM airports
    WHERE airports.city = "Fiftyville"
)
ORDER BY flt.hour, flt.minute
LIMIT 1;
-- +---------------+
-- |     city      |
-- +---------------+
-- | New York City |
-- +---------------+
-- ########################################################################################################################################################################################################

-- Conclusion: The flight that the theft was onboard landed in New York City. So, the theft escaped to New York City.

-- ########################################################################################################################################################################################################


-- Who is the theft's accomplice?
-- Who picked up the phone call from the theft and booked the plane ticket for him?
SELECT name FROM people AS ppl
JOIN phone_calls AS call ON call.receiver = ppl.phone_number
WHERE call.year = 2021 AND call.month = 7 AND call.day = 28 AND call.duration < 60 AND call.caller = (
    SELECT phone_number FROM people AS ppl
    WHERE ppl.name = "Bruce"
);
-- +-------+
-- | name  |
-- +-------+
-- | Robin |
-- +-------+
-- ########################################################################################################################################################################################################

-- Conclusion: The theft's accomplice is Robin

-- ########################################################################################################################################################################################################