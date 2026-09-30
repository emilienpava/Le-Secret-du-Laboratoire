from app.domain.room import Room
from app.domain.item import Item
from app.domain.door import Door
from app.domain.code_puzzle import CodePuzzle
from app.domain.hash_puzzle import HashPuzzle

room1 = Room(
    id="room1",
    name="Salle d'accueil",
    description="Les joueurs découvrent le laboratoire.",
    items=[
        Item(
            id="key1",
            name="Clé",
            description="Une vieille clé trouvée sur une table."
        ),
        Item(
            id="computer1",
            name="Ordinateur",
            description="Un ordinateur encore allumé."
        ),
        Item(
            id="document1",
            name="Document",
            description="Un document contenant des informations mystérieuses."
        )
    ],
    doors=[
        Door(
            id="door1",
            name="Porte vers le laboratoire",
            description="Une porte verrouillée menant au laboratoire.",
            is_locked=True,
            required_item_id="key1"
        )
    ],
    puzzles=[]
)

room2 = Room(
    id="room2",
    name="Laboratoire",
    description="Le laboratoire contient des expériences abandonnées et plusieurs indices.",
    items=[
        Item(
            id="flask1",
            name="Fiole",
            description="Une fiole contenant un liquide étrange."
        ),
        Item(
            id="card1",
            name="Carte magnétique",
            description="Une carte permettant probablement d'ouvrir certaines portes."
        ),
        Item(
            id="chest1",
            name="Coffre",
            description="Un coffre verrouillé avec un clavier numérique."
        )
    ],
    doors=[
        Door(
            id="door2",
            name="Porte vers la salle informatique",
            description="Une porte sécurisée menant à la salle informatique.",
            is_locked=True,
            required_item_id="card1"
        )
    ],
    puzzles=[
        CodePuzzle(
            id="puzzle1",
            name="Code du coffre",
            description="Le coffre demande un code à quatre chiffres.",
            secret_code="1234"
        )
    ]
)

room3 = Room(
    id="room3",
    name="Salle informatique",
    description="Une salle remplie d'ordinateurs où les joueurs doivent pirater le système.",

    items=[
        Item(
            id="computer2",
            name="Ordinateur",
            description="Un ordinateur connecté au système du laboratoire."
        ),
        Item(
            id="usb1",
            name="Clé USB",
            description="Une clé USB contenant des données importantes."
        ),
        Item(
            id="keyboard1",
            name="Clavier",
            description="Un clavier permettant d'interagir avec l'ordinateur."
        )
    ],

    doors=[
        Door(
            id="door3",
            name="Porte vers la salle de sortie",
            description="La dernière porte du laboratoire.",
            is_locked=True,
            required_item_id="usb1"
        )
    ],

    puzzles=[
        HashPuzzle(
            id="puzzle2",
            name="Mot de passe du système",
            description="Le système demande un mot de passe.",
            expected_hash="52b797a276d825aaa28f449f1d35682bd4d271f6455be84e3869cdd7aed2ca03"
        )
    ]
)

room4 = Room(
    id="room4",
    name="Salle de sortie",
    description="La dernière salle du laboratoire. La porte permet enfin de s'échapper.",
    items=[],
    doors=[],
    puzzles=[]
)