#!/usr/bin/python3
""" This script test deletets cities feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_st = fs.all(State)
print("All States: {}".format(len(all_st.keys())))
for state_key in all_st.keys():
    print(all_st[state_key])

# Create a new State
nw_state = State()
nw_state.name = "California"
fs.new(nw_state)
fs.save()
print("New State: {}".format(nw_state))

# All States
all_st = fs.all(State)
print("All States: {}".format(len(all_st.keys())))
for state_key in all_st.keys():
    print(all_st[state_key])

# Create another State
other_state = State()
other_state.name = "Nevada"
fs.new(other_state)
fs.save()
print("Another State: {}".format(other_state))

# All States
all_st = fs.all(State)
print("All States: {}".format(len(all_st.keys())))
for state_key in all_st.keys():
    print(all_st[state_key])

# Delete the new State
fs.delete(nw_state)

# All States
all_st = fs.all(State)
print("All States: {}".format(len(all_st.keys())))
for state_key in all_st.keys():
    print(all_st[state_key])
