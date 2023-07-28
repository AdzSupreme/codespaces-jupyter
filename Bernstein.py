#!/usr/bin/env python
# coding: utf-8

# In[25]:


from qiskit import *
from qiskit.tools.monitor import job_monitor
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_provider import IBMProvider
from qiskit_ibm_provider import least_busy
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram

provider = IBMProvider(instance='ibm-q/open/main')


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


secret_number = '11101001'


# In[21]:


secret_finder = QuantumCircuit(len(secret_number)+1, len(secret_number))


# In[22]:


secret_finder.h(range(len(secret_number)))


# In[23]:


secret_finder.x(len(secret_number))
secret_finder.h(len(secret_number))

secret_finder.barrier()

for ii, yesno in enumerate(reversed(secret_number)):
    if yesno == '1':
        secret_finder.cx(ii, len(secret_number))
        
secret_finder.barrier()
secret_finder.h(range(len(secret_number)))

secret_finder.barrier()
secret_finder.h(3)
secret_finder.measure(range(len(secret_number)), range(len(secret_number)))


# In[24]:


secret_finder.draw(output = 'mpl', initial_state = True)


# In[19]:


comp = provider.get_backend('ibmq_qasm_simulator')
job = execute(secret_finder, backend=comp, shots=1).result()
counts = job.get_counts()
print(counts)


# In[10]:


for string, digit in enumerate(secret_number):
    if digit == "1":
        print("1")
    else:
        print("0")


# In[ ]:




