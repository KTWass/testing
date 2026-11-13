from drafter import *
from dataclasses import dataclass

set_website_title("Pet")
set_site_information(
    author="Wassil",
    description="Testing deploy.",
    sources="Thanks to the Drafter docs and my study group.",
    planning=["Planning.pdf", "Design.pdf"],
    links=["https://github.com/KTWass/testing/blob/main/Planning.pdf","https://github.com/KTWass/testing/blob/main/Design.pdf"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    hunger: int
    energy: int


@route
def index(state: State) -> Page:
    return Page(state, [
        "Hunger: " + str(state.hunger) + "\n",
        "Energy: " + str(state.energy) + "\n",        
        "Mood: " + pet_mood(state) + "\n",
        Button("Feed", "feed"),
        Button("Play", "play"),
        Button("Rest", "rest")
    ])

@route
def feed(state: State) -> Page:
    state.hunger = state.hunger + 3
    if state.hunger < 0:
        state.hunger = 0
    return index(state)

@route
def play(state: State) -> Page:
    state.energy = state.energy - 3
    state.hunger = state.hunger + 2
    if state.energy < 0:
        state.energy = 0
    return index(state)


@route
def rest(state: State) -> Page:
    state.energy = state.energy + 3
    if state.energy > 10:
        state.energy = 10
    return index(state)

def pet_mood(state: State) -> str:
    if state.hunger > 6:
        return "hungry"
    if state.energy < 3:
        return "sleepy"
    return "happy"

assert_equal(pet_mood(State(8, 5)), "hungry")
assert_equal(pet_mood(State(2, 1)), "sleepy")
assert_state(feed(State(1, 5)), State(0, 5))
assert_has(index(State(5, 5)), "Mood: happy")

start_server(State(5, 5))



