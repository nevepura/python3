map = {
    "corridor" : {
        "links" : {
            "armory",
            "bridge",
        }
    },
    "armory" : {
        "links" : {
            "corridor",
        }
    },
    "bridge" : {
        "links" : {
            "corridor",
            "hangar",
        }
    },
    "hangar" : {
        "links" : {
            "bridge",
        }
    }
}

# potrei anche creare una classe e istanziare le varie stanze.
# tanto le stanze sono tutte uguali per comportamento