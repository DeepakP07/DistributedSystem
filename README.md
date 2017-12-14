CS7NS1 (Scalable Computing) -- Assignment 3 # Distributed_File_System.
========================================
***Student ID:17310212 Name: Deepak Purohit

Code is written in Python 2.7, To run this code Linux system is preferred.
This project is still in beta and can run and use it for small scale.
I have made this project referring few other projects/examples and some websites for completion of this Assignment.


Compile
Bash script that starts up a directory, locking, replication manager and file server on different ports on localhost

bash compile.sh
[starting_port] [no_severs] [no_copies]

User will be prompted to enter a start port number, amount of replicant managers and how many replicas each manager will have.
Starting port 8000 is recommended as Locking server is put on port 8888.

Test

python client.py [starting_port]
starting port must be the same as compile.


Implementation:

Follow of events:

Client -> Directory: Looking or Creating port number for a folder name

Client <- Directory: Reply with a port number if this folder name already exists or picks a server at random to now host till on

Client -> Replication Manager: Query's replication using port from directory. Replication manager holds ports of all the copies of the file. It also interacts with locking server for file locking

Replication Manager -> Locking Server: Request lock on file

Replication Manager <- Locking Server: Successful lock

Replication Manager -> Primary, executes query

Replication Manager <- Primary, success

Client < - Replication Manager: Replies with result of the query.

  Replication -> Secondary , etc ... Up till number of Copies (Partial Ordering )

  Replication Manager -> Unlocking Server: Request unlock on file

  Replication Manager <- Unlocking Server: Successful unlock
