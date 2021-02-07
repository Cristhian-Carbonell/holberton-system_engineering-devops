# Payment service incident report
-----------------------------------------
On December 12, 2020, we experienced a payment service outage. Today we provide the incident report specifying the condition of the fault and our repair.

## Issue Summary

On December 12, 2020, from 9:46 a.m. at 10:15 p.m. (UTC-5), our payment services were interrupted for 29 minutes. This affected the purchase of products, where the customer was looking for the product, but when buying it an error occurred, the product search services and other services worked normally. the problem affected 100% of customers, reducing sales.

## Chronology

On 12/30/2020 from 9:46 am (UTC-5) and 10:25 am our collection services are not available
collection services. It was not possible to complete purchases and customers received an error message when trying to load their credit card

- 9:47am the failure of the collection service was reported
- 9:50am we proceed to the verification, where it was observed that the maintenance configuration produced the error
- 10:00am later we observed that the database could not be connected, the server was overloaded, the RAID data replication occupied all the system resources
- 10:10am we proceed to stop data replication by removing the disk
10:15 the database service is back online and our collection service begins to recover 

## Root cause

The payment service depends on a MySQL database hosted by an external service. During a scheduled maintenance exercise, the database team realized that a server's disks were having problems, so it was decided to replace them.
Normally this should not be a problem as we are using RAID 5, but it also seemed that there was a wrong configuration in the RAID and the data replication was particularly slow. By replacing one of the disks, data replication consumed all system resources and this caused a bottleneck on the database servers, directly affecting the performance of our billing servers.

Our engineering teams were alerted that the billing service was showing a large number of errors at the same time that data replication began.
5 minutes later, the maintenance team detected the problem and decided to stop data replication by removing the new disk. a few minutes later the database service was working properly, and our collections services began to recover. after 35 minutes, all our services were working normally

Once the replication was stopped and the disk removed, the RAID configuration was reviewed and the problem with the configuration was found. The database team replicated this same scenario on a test server and was able to reproduce the problem. After making the configuration change and testing that replication does not affect service on the test server, the same change was made on the production server. The production server behaved as expected and the RAID is working properly.
Our configuration system has been updated so that this error does not happen again
