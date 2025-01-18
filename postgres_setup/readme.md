# Postgres Installation & Setup

## Installation
## Postgres Concepts

- **Client/Server Architecture**
- **Postgres Cluster**
  - A `directory` on the machine running the server that stores data and configuration files
- **Postgres Server**
  - A postgres server handles the data of single cluster
  - Clients connect to the server via network (TCP/IP)
    - Send commands and receive results
    - per default the network port for postgres is `5432`

### Configuration

By default postgres configuration files are stored in the cluster directory, but some installations put the configuration into a separate folder. There are two main configuration files that are of interest:

- `postgresql.conf` - this is the main configuration file for a postgres clusters.
- `pg_hba.conf` - in this file you setup rules that determine which IP addresses can access the server and what authentication methods they are allowed to use

#### Network access

The default setting in most installations is that you are

### Starting & Stopping the Postgres Server
