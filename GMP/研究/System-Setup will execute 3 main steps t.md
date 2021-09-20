System-Setup will execute 3 main steps to setup SAP System Y2Y,
specified by template PAYROLL_LARGE_HA

1. Reserving Blades and/or installing needed VirtualMachines

Installing VirtualMachine with 32.0 GB RAM, 8 cores, 20.0 GB swap
Installing VirtualMachine with 32.0 GB RAM, 8 cores, 20.0 GB swap
Installing VirtualMachine with 32.0 GB RAM, 8 cores, 20.0 GB swap


2. 'Providing System Resources' for System Y2Y:

Create SAP System in Inventory
Create LDAP entries
Create virtual IPs
Create or reuse vFiler
Create SAP System Volumes


3. 'Assign Server' for all Instances of System Y2Y to relevant hosts:

Create SAP-Instances in Inventory
Start virtual IPs of SAP-Instances on hosts
Mount all relevant Volumes on hosts 


