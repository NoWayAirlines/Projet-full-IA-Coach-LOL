"""
builds.py — Builds détaillés avec chemins d'items complets + ajustements selon l'ennemi.
Source : u.gg / lolalytics (patch 2025).
"""

BUILDS = {

    # ══════════════════════════════════════════════════════════════════════════
    # ADC
    # ══════════════════════════════════════════════════════════════════════════

    "Jinx": {
        "role": "ADC (Bot Lane)",
        "playstyle": (
            "Hypercarry late game. Très faible early, dévastatrice à partir du 2e-3e item. "
            "Ne prends pas de risques avant d'avoir Kraken Slayer + Hurricane. "
            "Ton ult (Super Mega Death Rocket!) est global : surveille la minimap."
        ),
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Eyeball Collection | Treasure Hunter",
        },
        "skill_order": "Monter R dès que possible. Puis Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",

        "build_paths": {
            "standard (comp équilibrée)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword (350g) → Pickaxe (875g) → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal (1050g) → Runaan's Hurricane",
                    "Infinity Edge (3400g)": "BF Sword (1300g) → Pickaxe (875g) → Cloak of Agility (600g) → Infinity Edge",
                    "Phantom Dancer (2600g)": "Zeal (1050g) → Phantom Dancer",
                    "Lord Dominik's Regards (3000g)": "Last Whisper (1450g) → Lord Dominik's Regards",
                    "Bloodthirster (3400g)": "BF Sword (1300g) → Bloodthirster",
                },
                "premier_retour": "Accroche Long Sword (350g). Si 875g → Pickaxe. Si 1600g → Pickaxe + Dagger.",
            },
            "vs tanks (Urgot, Malphite, Ornn...)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Mortal Reminder", "Phantom Dancer"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's Hurricane",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak of Agility → Infinity Edge",
                    "Lord Dominik's Regards (3000g)": "Last Whisper (1450g) → Lord Dominik's",
                    "Mortal Reminder (2500g)": "Last Whisper (1450g) → Mortal Reminder (si beaucoup de heal ennemi)",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                },
                "note": "Kraken Slayer fait des vrais dégâts aux tanks. Lord Dominik's Regards ignore la moitié de l'armure adverse.",
            },
            "vs assassins (Zed, Talon, Katarina...)": {
                "ordre": ["Galeforce", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Guardian Angel", "Bloodthirster"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer (1100g) → BF Sword (1300g) → Galeforce",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                    "Guardian Angel (3200g)": "Cloth Armor (300g) → Pickaxe (875g) → Guardian Angel",
                },
                "note": "Galeforce te donne un dash pour fuir les assassins. Guardian Angel pour la résurrection.",
            },
            "vs healers (Soraka, Yuumi, Aatrox...)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Mortal Reminder", "Lord Dominik's Regards", "Phantom Dancer"],
                "chemins": {
                    "Mortal Reminder (2500g)": "Last Whisper (1450g) → Mortal Reminder — applique Grievous Wounds (-40% heal)",
                },
                "note": "Prends Mortal Reminder avant Lord Dominik's si l'ennemi a beaucoup de heal.",
            },
        },

        "matchup_jinx_vs_urgot": (
            "Urgot est un juggernaut tanky avec armor naturel et Purge (W) qui mitraille. "
            "Jinx est en désavantage en lane early — évite les trades courts. "
            "BUILD recommandé vs Urgot : Kraken Slayer → Runaan's Hurricane → Infinity Edge → Lord Dominik's Regards → Mortal Reminder → Phantom Dancer. "
            "Kraken Slayer perce les tanks, Runaan permet de hitter plusieurs cibles avec ses passifs, "
            "Lord Dominik's ignore l'armure d'Urgot. "
            "En teamfight : reste à distance max avec Fishbones (rockets Q). "
            "Utilise Flame Chompers! (E) pour stopper le dash/engage d'Urgot."
        ),

        "tips": [
            "Utilise Pow-Pow (attaque rapide, Q vers minigun) pour farmer en lane.",
            "Fishbones (rockets, Q vers lance-roquettes) pour le poke et les teamfights AoE.",
            "Flame Chompers! (E) : pose-les sous toi pour empêcher les dives.",
            "Ton passif Excited! : un kill ou assist te donne AS + MS — enchaîne les kills.",
            "Ton ult est global. Lance-le sur des ennemis bas HP repérés sur la minimap.",
        ],
    },

    "Caitlyn": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Sniper, domination early, poke, contrôle de zone.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo ou Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Galeforce", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Mortal Reminder"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer (1100g) → BF Sword → Galeforce",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                },
            },
        },
        "tips": [
            "Yordle Snap Trap (W) : pose les pièges sur les buissons et autour des objectifs.",
            "Headshot (passif) : tous les 6 coups, ton auto fait x2 dégâts.",
            "En teamfight, vise toujours les ennemis piégés par ton E ou tes W.",
        ],
    },

    "Jhin": {
        "role": "ADC (Bot Lane)",
        "playstyle": "4 balles, burst, assassin-ADC. Forte la 4e balle.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Absolute Focus | Gathering Storm",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Galeforce", "The Collector", "Infinity Edge", "Mortal Reminder", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer → BF Sword → Galeforce",
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5% HP",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                },
            },
        },
        "tips": [
            "La 4e balle scale sur ton AD total — plus tu as d'AD, plus elle fait de dégâts.",
            "Ne gaspille pas ta 4e balle sur un minion. Reload = vulnérabilité.",
            "Deadly Flourish (W) : root l'ennemi s'il a été touché par un allié.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TOP
    # ══════════════════════════════════════════════════════════════════════════

    "Malphite": {
        "role": "Top Lane / Support",
        "playstyle": "Tank CC, engage AoE one-shot avec R, frontline inaccessible. Powerspike fort au R lvl 6.",
        "summoner_spells": "Flash + Teleport (ou Ignite si lane agressive)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery) — poke en lane | ou Grasp of the Undying (Resolve) — sustain",
            "sorcery": "Manaflow Band | Transcendence | Scorch (poke) ou Gathering Storm (scaling)",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > E > W > Q",
        "starting_items": "Doran's Ring + Health Potion x2 (AP) ou Doran's Shield + Health Potion (tank)",
        "build_paths": {
            "full tank (engage teamfight)": {
                "ordre": ["Sunfire Aegis", "Thornmail", "Warmog's Armor", "Force of Nature", "Randuin's Omen", "Abyssal Mask"],
                "chemins": {
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest (800g) → Sunfire Aegis",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail — Grievous Wounds si heal ennemi",
                    "Warmog's Armor (3000g)": "Giant's Belt (900g) → Warmog's — regen passive si +1100 HP",
                    "Force of Nature (2900g)": "Negatron Cloak (900g) → Force of Nature — si AP lourde",
                    "Randuin's Omen (2700g)": "Warden's Mail (1000g) → Giant's Belt → Randuin's — réduit les crits ennemis",
                    "Abyssal Mask (2300g)": "Spectre's Cowl → Abyssal Mask — booste AP alliés proches",
                },
                "premier_retour": "Rush Bami's Cinder (1000g) pour le sustain et les dégâts passifs.",
            },
            "AP (one-shot assassin)": {
                "ordre": ["Rod of Ages", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Ionian Boots of Lucidity"],
                "chemins": {
                    "Rod of Ages (2600g)": "Catalyst of Aeons (1100g) → Rod of Ages — scale sur 10 min",
                    "Shadowflame (3000g)": "Needlessly Large Rod (1250g) → Shadowflame — perce les boucliers",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's — +40% AP total",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard (1300g) → Zhonya's — stase après le R",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff — perce la MR",
                },
                "note": "Build AP = one-shot garanti au R si ennemi squishy. Risqué mais dévastateur.",
            },
            "vs Jayce (lane poke)": {
                "ordre": ["Rod of Ages", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Randuin's Omen"],
                "note": (
                    "Jayce est un lane bully à distance qui te poke en forme canon. "
                    "Rush Rod of Ages pour le sustain. Reste derrière tes minions pour éviter le poke. "
                    "Wait lvl 6 : ton R (Unstoppable Force) est un engage AoE instantané — Jayce ne peut pas l'esquiver. "
                    "Flash + R = kill assuré si Jayce est mal positionné."
                ),
            },
        },
        "counters": "Jayce, Kennen, Vayne Top (kite). Évite les ranged bully.",
        "strong_vs": "Yasuo, Tryndamere, Zed Top, Pantheon. Tous les melees sans dash.",
        "tips": [
            "Unstoppable Force (R) : engage AoE instantané, inévitable. Combo avec Flash pour surprendre.",
            "Ground Slam (E) : réduit l'AS des ennemis proches — parfait contre ADC et fighters AA-based.",
            "Thunderclap (W) : passif bouclier permanent. Actif = prochain AA + éclaboussures.",
            "En teamfight : R sur le maximum d'ennemis, priorité sur les carries ennemis.",
        ],
    },

    "Jayce": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Lane bully ranged, poke dominant, switch marteau/canon. Forte early, tombe en late.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision) — trades longs | ou Arcane Comet (Sorcery) — poke",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Long Sword + Health Potion x3 (agressif) ou Doran's Shield (safe)",
        "build_paths": {
            "standard (fighter)": {
                "ordre": ["Trinity Force", "The Collector", "Serylda's Grudge", "Edge of Night", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage (1100g) → Sheen (700g) → Stinger (1100g) → Trinity Force — powerspike massif",
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5% HP",
                    "Serylda's Grudge (3200g)": "Caulfield's Warhammer → Pickaxe → Serylda's — slow permanent sur Q",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield anti-engage",
                    "Lord Dominik's Regards (3000g)": "Last Whisper → Lord Dominik's — si tanks",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel — résurrection",
                },
                "premier_retour": "Rush Phage (1100g). Si 1300g → Sheen.",
            },
            "vs tanks": {
                "ordre": ["Trinity Force", "Void Staff", "Serylda's Grudge", "Lord Dominik's Regards", "Edge of Night", "Guardian Angel"],
                "note": "Ajoute Void Staff pour percer la MR si les tanks stackent de la résistance magique.",
            },
        },
        "counters": "Malphite (R inévitable), Camille, Irelia (post-6).",
        "strong_vs": "Garen, Malphite early (poke), Nasus, champions sans dash.",
        "tips": [
            "Forme Canon : poke à distance avec Q (Shock Blast) amplifié par W (Hyper Charge).",
            "Forme Marteau : engage, all-in, trades courts avec E (Thundering Blow) pour repousser.",
            "Switch forme intelligemment : poke en canon → all-in en marteau si ennemi low.",
            "Jayce tombe en late game — snowball ou impacter avant 25 min.",
        ],
    },
    # ══════════════════════════════════════════════════════════════════════════

    "Urgot": {
        "role": "Top Lane",
        "playstyle": "Juggernaut tanky-fighter. Domine la lane early/mid. Exécution au R.",
        "summoner_spells": "Flash + Ignite (agressif) ou Flash + Teleport (macro)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Shield + Health Potion (Longsword si agressif)",
        "build_paths": {
            "fighter (carry)": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage (1100g) → Sheen (700g) → Stinger (1100g) → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem (800g) → Giant's Belt (900g) → Sterak's Gage",
                    "Death's Dance (3300g)": "Caulfield's Warhammer (1100g) → Chain Vest (800g) → Death's Dance",
                    "Thornmail (2700g)": "Chain Vest (800g) → Bami's Cinder (1000g) → Thornmail — si heal ennemi",
                    "Force of Nature (2900g)": "Negatron Cloak (900g) → Force of Nature — si beaucoup d'AP ennemi",
                },
                "premier_retour": "Rush Phage (1100g) si possible, sinon Long Sword.",
            },
            "tank (résistance max)": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Randuin's Omen"],
                "chemins": {
                    "Heartsteel (2800g)": "Crystalline Bracer (800g) → Giant's Belt (900g) → Heartsteel",
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest (800g) → Sunfire Aegis",
                    "Warmog's Armor (3000g)": "Giant's Belt (900g) → Warmog's",
                },
            },
            "vs healing (Mundo, Soraka...)": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Thornmail", "Death's Dance", "Force of Nature", "Guardian Angel"],
                "note": "Rush Thornmail en 3e si beaucoup de heal ennemi. Grievous Wounds (-40% heal).",
            },
        },
        "counters": "Trundle, Fiora, Vayne (Top). Évite ces matchups si possible.",
        "strong_vs": "Garen, Malphite, Sett, Cho'Gath.",
        "tips": [
            "Purge (W) : mitraille pendant 4s, slow, root si ennemi proche. Utilise en échange court.",
            "Disdain (E) : dash + CC sur un ennemi derrière toi. Parfait pour interrompre les fuyards.",
            "Fear Beyond Death (R) : exécute les ennemis sous ~25% HP. Réactivable pour les tirer.",
            "Ta force vient de l'échange Purge (W) + Corrosive Charge (Q). Engage, Q, W, E si nécessaire.",
        ],
    },

    "Darius": {
        "role": "Top Lane",
        "playstyle": "Juggernaut, saignement (Hemorrhage), snowball, exécution Noxian Guillotine (R).",
        "summoner_spells": "Flash + Ghost (pour rattraper) ou Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Hullbreaker", "Thornmail", "Warmog's Armor"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's Gage",
                    "Death's Dance (3300g)": "Caulfield's Warhammer → Chain Vest → Death's Dance",
                    "Hullbreaker (3000g)": "Longsword → Pickaxe → Hullbreaker — pour split push",
                },
            },
        },
        "tips": [
            "Ton Q Decimate heal si tu touches le bord extérieur. Toujours viser avec le bord.",
            "5 stacks de Hemorrhage = passif Noxian Might (+bonus AD énorme).",
            "Ghost > Flash pour kiter les fuyards et rester en range pour le R.",
        ],
    },

    "Garen": {
        "role": "Top Lane",
        "playstyle": "Tank-fighter simple, silence Q, spin E, exécution R. Bon pour apprendre le top.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Revitalize",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Warmog's Armor", "Thornmail", "Force of Nature", "Dead Man's Plate"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's Gage",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's — active la regen passive",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MID
    # ══════════════════════════════════════════════════════════════════════════

    "Ahri": {
        "role": "Mid Lane",
        "playstyle": "Assassin-mage mobile, pick, roam. Fort au milieu de partie.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter (1300g) → Amplifying Tome → Luden's Tempest",
                    "Shadowflame (3000g)": "Amplifying Tome → Needlessly Large Rod (1250g) → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's — +40% AP",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard (1300g) → Zhonya's — si beaucoup d'AD",
                    "Void Staff (2800g)": "Blighting Jewel (1250g) → Void Staff — si ennemis résistants magie",
                },
                "premier_retour": "Rush Lost Chapter (1300g) pour la mana et le CDR.",
            },
            "vs tanks": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Void Staff", "Rabadon's Deathcap", "Zhonya's Hourglass"],
                "note": "Prends Void Staff en 3e si les ennemis stackent de la résistance magique.",
            },
        },
        "tips": [
            "Orb of Deception (Q) : touche à l'aller ET au retour. Vise pour maximiser.",
            "Charm (E) : immobilise et amplifie tes dégâts. Engage toujours avec E → Q → W.",
            "Spirit Rush (R) : 3 dash en 10s. Utilise pour engage, pourchasser ou fuir.",
        ],
    },

    "Zed": {
        "role": "Mid Lane / Top",
        "playstyle": "Assassin, burst one-shot, split push. Snowball violent.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Future's Market",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Long Sword + Health Potion x3",
        "build_paths": {
            "standard": {
                "ordre": ["The Collector", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards", "Serylda's Grudge"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5%",
                    "Youmuu's Ghostblade (3000g)": "Serrated Dirk → Caulfield's Warhammer (1100g) → Youmuu's",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — bouclier anti-sort",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's Fang — si boucliers ennemis",
                    "Lord Dominik's Regards (3000g)": "Last Whisper → Lord Dominik's — si tanks",
                    "Serylda's Grudge (3200g)": "Caulfield's Warhammer → Pickaxe → Serylda's — slow permanent",
                },
                "premier_retour": "Rush Serrated Dirk (1100g) pour le lethality.",
            },
        },
        "tips": [
            "Combo de base : W (shadow) → E (slow) → Q (shurikens) → R (ult) → reposition → Q + E → récupère W.",
            "Living Shadow (W) : échange avec ta shadow pour repositionner. Utilise pour fuir aussi.",
            "Death Mark (R) : ta marque explose après 3s. Assure le kill avant.",
        ],
    },

    "Lux": {
        "role": "Mid Lane / Support",
        "playstyle": "Mage burst longue portée, poke, snipe.",
        "summoner_spells": "Flash + Ignite (mid) | Flash + Exhaust (support)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Cut Down",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter → Amplifying Tome → Luden's",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's",
                },
            },
        },
        "tips": [
            "Light Binding (Q) : snare sur 2 cibles. Toujours Q avant R pour garantir le touch.",
            "Finales Funkeln (R) : très faible CD si tu touches. Utilise souvent.",
            "Passif Illumination : marque les ennemis, ton prochain auto double les dégâts.",
        ],
    },

    "Yasuo": {
        "role": "Mid Lane / Top",
        "playstyle": "Fighter carry, bouclier passif, critkeur, hypercarry.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Immortal Shieldbow", "Infinity Edge", "Kraken Slayer", "Phantom Dancer", "Death's Dance", "Guardian Angel"],
                "chemins": {
                    "Immortal Shieldbow (3400g)": "Caulfield's Warhammer → Pickaxe → Cloak → Immortal Shieldbow",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge — ne prends QUE si tu as 60%+ crit",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer — si tanks",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                    "Death's Dance (3300g)": "Caulfield's Warhammer → Chain Vest → Death's Dance",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel",
                },
                "note": "N'achète Infinity Edge QUE quand tu as déjà 60% de crit (= Shieldbow + Phantom Dancer).",
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JUNGLE
    # ══════════════════════════════════════════════════════════════════════════

    "Lee Sin": {
        "role": "Jungle",
        "playstyle": "Very strong early, invade, gank, carry early-mid. Tombe off en late.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "fighter": {
                "ordre": ["The Collector", "Youmuu's Ghostblade", "Death's Dance", "Sterak's Gage", "Serylda's Grudge", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector",
                    "Youmuu's Ghostblade (3000g)": "Serrated Dirk → Caulfield's Warhammer → Youmuu's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
    },

    "Vi": {
        "role": "Jungle",
        "playstyle": "Engage, dive sur le carry ennemi, tank-fighter.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Gustwalker Hatchling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
    },

    "Amumu": {
        "role": "Jungle / Support",
        "playstyle": "Tank CC, engage AoE, teamfight dominant. Simple à jouer.",
        "summoner_spells": "Flash + Smite (jungle) | Flash + Exhaust (support)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Gustwalker Hatchling (jungle) + Health Potion",
        "build_paths": {
            "tank": {
                "ordre": ["Sunfire Aegis", "Abyssal Mask", "Force of Nature", "Thornmail", "Warmog's Armor"],
                "chemins": {
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest → Sunfire Aegis",
                    "Abyssal Mask (2300g)": "Spectre's Cowl → Abyssal Mask — boost AP alliés proches",
                    "Force of Nature (2900g)": "Negatron Cloak → Force of Nature",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUPPORT
    # ══════════════════════════════════════════════════════════════════════════

    "Thresh": {
        "role": "Support",
        "playstyle": "Engage/peel, hook (Q), lanterne (W), versatile.",
        "summoner_spells": "Flash + Ignite (agressif) | Flash + Exhaust (peel)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > W > E > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Knight's Vow", "Redemption", "Mikael's Blessing"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Knight's Vow (2300g)": "Kindlegem → Giant's Belt → Knight's Vow",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                },
            },
        },
        "tips": [
            "Death Sentence (Q) : hook. Réactive immédiatement pour te propulser vers l'ennemi.",
            "Dark Passage (W) : lanterne pour te placer et sauver un allié. Toujours avoir une lanterne dispo.",
            "Thresh est un champion skill-cap — la qualité de ton Q détermine tout.",
        ],
    },

    "Lulu": {
        "role": "Support",
        "playstyle": "Enchanteur, boucliers, peel. Protège le hypercarry allié.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "enchanteur": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent Censer",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ADC SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Ezreal": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Poke ADC, kite, safe laner. Powerspike lent mais fort en late.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Manamune", "Serylda's Grudge", "Rabadon's Deathcap", "Shadowflame", "Ionian Boots of Lucidity"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — powerspike Q poke",
                    "Manamune (2900g)": "Tear of the Goddess (400g) — rush dès le départ → Manamune — scaling mana",
                    "Serylda's Grudge (3200g)": "Caulfield's → Pickaxe → Serylda's — slow sur Q",
                },
                "premier_retour": "Rush Tear of the Goddess (400g) immédiatement + Long Sword.",
            },
        },
        "tips": [
            "Mystic Shot (Q) : reset tous tes cooldowns si tu touche. Spam Q en permanence.",
            "Arcane Shift (E) : ton dash, garde-le pour esquiver les CC ou fuir.",
            "Joue safe early, scale sur 3 items. Ne prends pas de risques inutiles.",
        ],
    },

    "Ashe": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Utility ADC, kite, CC global, vision avec W.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Gathering Storm",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Mortal Reminder", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's — AoE slow avec passif Ashe",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Volley (W) : spam en lane pour le poke et la vision des buissons.",
            "Enchanted Crystal Arrow (R) : CC global. Utilise cross-map pour sauver un allié ou initier.",
            "Ton passif slow permanent = kite naturel. Reste à distance et attaque en reculant.",
        ],
    },

    "Draven": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Lane bully hyper agressif, snowball, one of the highest early damage ADC.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Infinity Edge", "Lord Dominik's Regards", "Phantom Dancer", "Bloodthirster", "Mortal Reminder"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Spinning Axes (Q) : attrape tes haches pour les relancer. Mouvement constant pour les récupérer.",
            "Snowball violent — si tu n'es pas fed avant 15 min, tu perds ton avantage.",
            "Ignore les stacks League of Draven si tu risques de mourir pour les récupérer.",
        ],
    },

    "Samira": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Assassin-ADC, all-in, style combo, R dévastateur en melee range.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Bloodline | Last Stand",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Immortal Shieldbow", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Immortal Shieldbow (3400g)": "Caulfield's → Pickaxe → Cloak → Shieldbow — survie en melee",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE — attend 60% crit",
                },
            },
        },
        "tips": [
            "Buildup style grade S (passif) avant de lancer Inferno Trigger (R).",
            "Wild Rush (E) : dash sur un ennemi ou allié, réinitialise sur kill.",
            "Joue agressivement, engage avec support, R dans le tas.",
        ],
    },

    "Tristana": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Hypercarry late, portée augmente avec les niveaux, reset sur kill.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Rapid Fire (Q) : AS massif pendant 7s. Toujours actif avant un trade.",
            "Rocket Jump (W) : jump sur ennemi (engage) ou en arrière (fuite). Reset sur kill/assist.",
            "Buster Shot (R) : repousse l'ennemi, stacks les bombes sur tour pour la demolish.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MID SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Akali": {
        "role": "Mid Lane / Top",
        "playstyle": "Assassin mobile, sustain en zone, burst très fort post-6.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Celerity | Waterwalking",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion (top) | Long Sword + potions (mid)",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator (1050g) → Hextech Rocketbelt — dash + burst",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase anti-assassin",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
                "premier_retour": "Rush Hextech Alternator (1050g).",
            },
        },
        "tips": [
            "Shroud (W) : zone invisible, utilise pour reset trades ou fuir.",
            "Combo : Q → E → Q (mark) → R1 → auto → R2 pour le burst complet.",
            "Powerspike fort au R lvl 6 — cherche le kill dès que tu l'as.",
        ],
    },

    "Viktor": {
        "role": "Mid Lane",
        "playstyle": "Mage scaling, zone control, upgrades progressifs, fort en late teamfight.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Cut Down",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass", "Sorcerer's Shoes"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter → Amplifying Tome → Luden's",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff — si MR ennemi",
                },
            },
        },
        "tips": [
            "Rush les upgrades de Viktor : Q → W → E dans l'ordre de priorité.",
            "Death Ray (E) : zone de dégâts + explosion après. Colle-le sur les groupes ennemis.",
            "Chaos Storm (R) : suit les ennemis, repositionne-le sur le carry adverse.",
        ],
    },

    "Katarina": {
        "role": "Mid Lane",
        "playstyle": "Assassin reset, snowball violent, AoE sur groupes, haut skill cap.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Domination",
            "secondary": "Sudden Impact | Treasure Hunter",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Long Sword + Health Potion x3",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator → Rocketbelt — dash + burst",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase pendant R",
                },
            },
        },
        "tips": [
            "Passif : chaque kill/assist reset Shunpo (E). Enchaîne les resets en teamfight.",
            "Daggers sur le sol = dégâts bonus si tu les ramasses ou Shunpo dessus.",
            "Contre les CC : Zhonya's pendant R pour éviter le one-shot.",
        ],
    },

    "Kassadin": {
        "role": "Mid Lane",
        "playstyle": "Late game hyper carry, très faible early, invincible à partir du lvl 11-16.",
        "summoner_spells": "Flash + Ignite (ou Teleport pour safer)",
        "runes": {
            "primary_keystone": "Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Tenacity | Last Stand",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion (safe) ou Doran's Ring",
        "build_paths": {
            "standard": {
                "ordre": ["Rod of Ages", "Seraph's Embrace", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Rod of Ages (2600g)": "Catalyst of Aeons (1100g) → Rod of Ages — rush, scale sur 10 min",
                    "Seraph's Embrace (2600g)": "Tear of the Goddess (400g) — rush aussi → Seraph's — mana infini",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
                "note": "Survive early (Fleet Footwork), scale lvl 11-16. Ne cherche pas à gagner avant.",
            },
        },
        "tips": [
            "Riftwalk (R) : cd très court, dash + dégâts. Spam en teamfight.",
            "Void Stone (P) : réduit les dégâts magiques de 15%. Bon vs mages.",
            "Joue ultra safe jusqu'au lvl 6. Rush Rod of Ages + Tear en priorité.",
        ],
    },

    "Ekko": {
        "role": "Mid Lane / Jungle",
        "playstyle": "Assassin-mage, mobilité, reset avec R, snowball solide.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Lich Bane", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator → Rocketbelt",
                    "Lich Bane (3000g)": "Sheen (700g) → Amplifying Tome → Lich Bane — empowered AA après sort",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                },
            },
        },
        "tips": [
            "Chronobreak (R) : revient en arrière, heal, burst. Utilise si tu es en danger ou pour finir.",
            "Timewinder (Q) : retour du boomerang = stun si 3 stacks passif sur ennemi.",
            "Parallel Convergence (W) : bouclier + stun si ennemi dedans. Engage dessus avec E.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TOP SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Aatrox": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Juggernaut sustain, revivre passif, poke avec Q, dominant en prolonged trades.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance — heal sur dégâts",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail — si beaucoup de heal ennemi",
                },
            },
        },
        "tips": [
            "Vise les bords extérieurs de Darkin Blade (Q) pour le maximum de dégâts.",
            "World Ender (R) : revive passif + heal massif. Active avant d'engager une fight.",
            "Infernal Chains (W) : slow + pull si ennemi reste dedans. Utilise pour Q ou E combo.",
        ],
    },

    "Fiora": {
        "role": "Top Lane",
        "playstyle": "Duelist 1v1 imbattable, splitpush, execute les tanks via Vitals.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Ravenous Hydra", "Death's Dance", "Guardian Angel", "Sterak's Gage", "Wit's End"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Ravenous Hydra (3300g)": "Tiamat (1325g) → Pickaxe → Ravenous Hydra — sustain + waveclear",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel",
                },
            },
        },
        "tips": [
            "Vitals (passif) : toucher les 4 Vitals avec Grand Challenge (R) = heal massif zonal.",
            "Riposte (W) : parry un CC — crucial contre les all-in. Pratique le timing.",
            "Lunge (Q) : 2 charges, reset sur hit de Vital. Combo Q → touche Vital → Q de retour.",
        ],
    },

    "Camille": {
        "role": "Top Lane / Jungle",
        "playstyle": "Duelist mobile, lock-down R, splitpush dangereux.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Thornmail", "Force of Nature"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — powerspike majeur",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "Hookshot (E) : wall-hook + dash sur ennemi. Engage ou fuite.",
            "Hextech Ultimatum (R) : emprisonne un ennemi 1v1. Utilise sur le carry isolé.",
            "Precision Protocol (Q) : empowered AA avec slow. Double Q si tu attends 1.5s.",
        ],
    },

    "Irelia": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Duelist reset sur minions, fort post-4-5 stacks passif.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Wit's End", "Thornmail"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                    "Wit's End (2900g)": "Negatron Cloak → Recurve Bow → Wit's End — si beaucoup d'AP",
                },
            },
        },
        "tips": [
            "Bladesurge (Q) : reset sur kill de minion/champion. Manage tes minions pour entrer en range.",
            "Stack ton passif (Ionian Fervor) à 5 avant d'engager le carry adverse.",
            "Flawless Duet (E) : CC AoE entre 2 lames. Place les 2 lames de chaque côté de l'ennemi.",
        ],
    },

    "Mordekaiser": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Tank-mage, 1v1 en Death Realm, résistant, AoE dégâts.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Riftmaker", "Rylai's Crystal Scepter", "Demonic Embrace", "Shadowflame", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Riftmaker (3200g)": "Hextech Alternator → Kindlegem → Riftmaker — true damage passif",
                    "Rylai's Crystal Scepter (2600g)": "Hextech Alternator → Giant's Belt → Rylai's — slow permanent",
                    "Demonic Embrace (3000g)": "Blighting Jewel → Giant's Belt → Demonic — burn + survie",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
            },
        },
        "tips": [
            "Realm of Death (R) : emmène l'ennemi en 1v1. Tu voles ses stats — engage sur le carry.",
            "En Death Realm, focus stats volées. Si tu peux pas kill, au moins fais-le perdre du temps.",
            "Indestructible (W) : absorbe dégâts en bouclier. Actif APRÈS avoir pris des dégâts.",
        ],
    },

    "Nasus": {
        "role": "Top Lane",
        "playstyle": "Scaling hyper carry, farm les stacks, invincible en late game.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > W > E > Q (farm Q UNIQUEMENT)",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Warmog's Armor", "Thornmail", "Force of Nature", "Hullbreaker"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — Sheen = Q one-shot",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's — regen passive",
                    "Hullbreaker (3000g)": "Long Sword → Pickaxe → Hullbreaker — splitpush inaccessible",
                },
            },
        },
        "tips": [
            "Farm Q sur tout — minions, jungle, objectives. Objectif : 300+ stacks avant 20 min.",
            "Wither (W) : slow AS et MS massif — colle l'ADC avec ça.",
            "Joue ultra safe early pour farmer. Splitpush en side lane à partir du lvl 11.",
        ],
    },

    "Sett": {
        "role": "Top Lane / Support / Jungle",
        "playstyle": "Juggernaut tank, tanky fighter, W one-shot avec true damage.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "The Show Stopper (R) : grab + smash. Lance un ennemi dans ses propres alliés.",
            "Haymaker (W) : accumule grit (dégâts reçus), release = true damage + bouclier.",
            "Stack le grit en prenant des dégâts, puis W pour le burst en true damage.",
        ],
    },

    "Tryndamere": {
        "role": "Top Lane / Jungle",
        "playstyle": "Splitpush inaccessible, invincible avec R, hypercarry crit.",
        "summoner_spells": "Flash + Ignite (ou Ghost + Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Phantom Dancer", "Infinity Edge", "Mortal Reminder", "Guardian Angel", "Death's Dance"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer — bouclier + AS",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE — attend 60% crit",
                },
            },
        },
        "tips": [
            "Undying Rage (R) : invincible 5s. Active sous 1 HP pour survivre et tuer.",
            "Splitpush en side lane — tu coupes les tours inaccessible 1v1.",
            "Spinning Slash (E) : dash sur l'ennemi ou fuite. Reset CD si tu kills.",
        ],
    },

    "Volibear": {
        "role": "Top Lane / Jungle",
        "playstyle": "Tank-fighter engage, jump avec R sur une tourelle, fort en teamfight.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Bone Plating | Overgrowth",
            "secondary_tree": "Precision",
            "secondary": "Legend: Tenacity | Last Stand",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Sterak's Gage"],
                "chemins": {
                    "Heartsteel (2800g)": "Crystalline Bracer → Giant's Belt → Heartsteel — HP massif",
                    "Sunfire Aegis (3200g)": "Bami's Cinder → Chain Vest → Sunfire",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                    "Thornmail (2700g)": "Chain Vest → Bami's → Thornmail",
                },
            },
        },
        "tips": [
            "The Relentless Storm (R) : jump qui désactive les tourelles. Engage sous tour en sécurité.",
            "Sky Splitter (E) : cage lightning — CC + bouclier si tu es dans la zone.",
            "Thundering Smash (Q) : charge + stun si l'ennemi est slow. Combo Q → W (bite).",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JUNGLE SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Kayn": {
        "role": "Jungle",
        "playstyle": "Deux formes : Rhaast (tank) ou Shadow Assassin (assassin). S'adapte à l'ennemi.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision) — Rhaast | Electrocute (Domination) — SA",
            "precision": "Triumph | Legend: Tenacity | Last Stand (Rhaast)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter (SA)",
            "secondary_tree": "Sorcery",
            "secondary": "Celerity | Waterwalking",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "Rhaast (tank, vs full AD/tanky)": {
                "ordre": ["Goredrinker", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Goredrinker (3300g)": "Caulfield's → Kindlegem → Goredrinker — AoE heal",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
                "note": "Rhaast : farm les champions AD/tanky en lane pour transformer plus vite.",
            },
            "Shadow Assassin (vs squishy/AP)": {
                "ordre": ["The Collector", "Serpent's Fang", "Edge of Night", "Serylda's Grudge", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's Fang — anti-boucliers",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night",
                },
                "note": "SA : farm les mages/assassins pour transformer. Playstyle one-shot.",
            },
        },
        "tips": [
            "Farm les bons champions pour orienter ta transformation (AD → Rhaast, AP → SA).",
            "Umbral Trespass (R) : entre dans un ennemi, heal si Rhaast, burst si SA.",
            "Darkin Scythe (Q) : passe à travers les murs. Mobility jungle extrême.",
        ],
    },

    "Kha'Zix": {
        "role": "Jungle",
        "playstyle": "Assassin isolate, one-shot les cibles seules, évolue ses sorts.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Precision",
            "secondary": "Triumph | Legend: Tenacity",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["The Collector", "Serpent's Fang", "Edge of Night", "Serylda's Grudge", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector — exécute sous 5%",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's — anti-boucliers",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield",
                },
                "evolution": "1er évolution : Q (Taste Their Fear) — dégâts isolate x2. 2e : E (Leap) — reset sur kill. 3e : W (Void Spike) — heal massif.",
            },
        },
        "tips": [
            "Isolate : cible toujours un ennemi SEUL (passif). Dégâts doublés.",
            "Evolved Q = one-shot quasi garanti sur une cible isolée.",
            "Void Assault (R) : invisibilité 3 charges. Utilise pour entrer/sortir d'un fight.",
        ],
    },

    "Hecarim": {
        "role": "Jungle",
        "playstyle": "Engage rapide, MS = dégâts, tank-fighter, fort ganks lvl 3.",
        "summoner_spells": "Flash (ou Ghost) + Smite",
        "runes": {
            "primary_keystone": "Phase Rush (Sorcery)",
            "sorcery": "Nimbus Cloak | Celerity | Waterwalking",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Gustwalker Hatchling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Dead Man's Plate", "Force of Nature", "Warmog's Armor", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — MS + dégâts passif",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Dead Man's Plate (2900g)": "Chain Vest → Giant's Belt → Dead Man's — MS + engage",
                    "Force of Nature (2900g)": "Negatron Cloak → Force of Nature — si AP lourde",
                },
            },
        },
        "tips": [
            "Rampage (Q) : AoE rapide, stack = encore plus rapide. Farm rapide.",
            "Devastating Charge (E) : accélération + knockback. Lance tes ganks avec E → R.",
            "Onslaught of Shadows (R) : engage AoE fear. Vise le groupe ennemi.",
        ],
    },

    "Graves": {
        "role": "Jungle",
        "playstyle": "Fighter jungler, DPS burst, safe avec dash, fort duel.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Lord Dominik's Regards", "Serylda's Grudge"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "Smoke Screen (W) : zone aveugle + slow. Pose dans les pieds de l'ennemi en fight.",
            "Quickdraw (E) : dash qui recharge 1 cartouche. Kite et dash intelligemment.",
            "Graves ne peut tirer qu'avec 2 cartouches — recharge entre chaque burst.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUPPORT SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Leona": {
        "role": "Support",
        "playstyle": "Tank engage, CC chain massive, frontline inaccessible.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > E > W > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Force of Nature", "Knight's Vow"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                },
            },
        },
        "tips": [
            "Combo engage : E (Zenith Blade) → W (Shield of Daybreak) pour le stun immédiat.",
            "Solar Flare (R) : AoE CC. Vise sur le carry ennemi ou dans le groupe.",
            "Tank tout — ton rôle est de prendre les dégâts et CC le maximum.",
        ],
    },

    "Nautilus": {
        "role": "Support / Jungle",
        "playstyle": "Engage tank, hook (Q), CC chain énorme, frontline.",
        "summoner_spells": "Flash + Ignite (ou Exhaust)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > W > E > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Force of Nature", "Redemption"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                    "Thornmail (2700g)": "Chain Vest → Bami's → Thornmail — si heal ennemi",
                },
            },
        },
        "tips": [
            "Dredge Line (Q) : hook sur ennemi ou terrain. Pratique le hook à travers les murs.",
            "Depth Charge (R) : CC global qui suit l'ennemi. Utilise sur le carry ennemi.",
            "Passif : première auto sur chaque ennemi = root. Colle-les et auto d'abord.",
        ],
    },

    "Morgana": {
        "role": "Support / Mid Lane",
        "playstyle": "CC long (Q), bouclier anti-CC (E), utility tank.",
        "summoner_spells": "Flash + Exhaust (support) | Flash + Ignite (mid)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "support": {
                "ordre": ["Locket of the Iron Solari", "Redemption", "Zhonya's Hourglass", "Mikael's Blessing", "Ardent Censer", "Knight's Vow"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase pendant R",
                },
            },
        },
        "tips": [
            "Dark Binding (Q) : root 3s le plus long du jeu. Visée critique à maîtriser.",
            "Black Shield (E) : bouclier anti-CC sur allié. Timing crucial contre engage.",
            "Soul Shackles (R) : AoE CC chain. Reste dans le groupe — Zhonya's pour survivre.",
        ],
    },

    "Soraka": {
        "role": "Support",
        "playstyle": "Heal bot, sustain extrême, Silence (E), ult global (R).",
        "summoner_spells": "Flash + Exhaust (ou Ignite si agressif)",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing", "Chemtech Putrifier"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent",
                    "Chemtech Putrifier (2300g)": "Forbidden Idol → Amplifying Tome → Chemtech — Grievous Wounds sur heal",
                },
                "note": "Prends Chemtech Putrifier si l'ennemi a beaucoup de heal.",
            },
        },
        "tips": [
            "Astral Infusion (W) : coûte 10% HP max. Heal sans limite si tu restes en vie.",
            "Wish (R) : heal global. Utilise dès qu'un allié est en danger partout sur la map.",
            "Equinox (E) : Silence AoE + zone. Utilise pour stopper les engages ou les recalls.",
        ],
    },

    "Nami": {
        "role": "Support",
        "playstyle": "Enchanteur engage/peel, heal, buff AA alliés, fort CC avec Q.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing", "Shurelya's Battlesong"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent",
                },
            },
        },
        "tips": [
            "Aqua Prison (Q) : bubble qui stun. Vise au sol, difficile à toucher — entraîne-toi.",
            "Tidecaller's Blessing (E) : buff AA allié avec slow + dégâts. Pose sur l'ADC en fight.",
            "Tidal Wave (R) : slow AoE global. Utilise pour engage depuis loin ou disengage.",
        ],
    },

    "Pyke": {
        "role": "Support / Mid Lane",
        "playstyle": "Assassin support, hook, execute avec R (or pour toute l'équipe), roam.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Legend: Tenacity",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Umbral Glaive", "Serrated Dirk", "Edge of Night", "Serpent's Fang", "Axiom Arc", "Sorcerer's Shoes"],
                "chemins": {
                    "Umbral Glaive (2300g)": "Serrated Dirk → Long Sword → Umbral Glaive — ward clearer",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield",
                    "Axiom Arc (3000g)": "Caulfield's → Serrated Dirk → Axiom Arc — réduit CD ultime sur kill",
                },
            },
        },
        "tips": [
            "Death from Below (R) : exécute sous le seuil HP. L'allié qui assist reçoit aussi l'or.",
            "Bone Skewer (Q) : hold = lancer, tap = pull. Pull en buisson pour l'engage.",
            "Regen rapide hors combat — reste à la frontline pour tanker puis regen.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NOUVEAUX CHAMPIONS — ADC
    # ══════════════════════════════════════════════════════════════════════════

    "Kai'Sa": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Hypercarry hybride AD/AP. Powerspike énorme après évolutions. Scale infiniment.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R dès que possible. Q > W > E. Évoluer Q en premier (100 bonus AD), puis W (100 AP).",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard (crit)": {
                "ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Nashor's Tooth", "Rabadon's Deathcap", "Zhonya's Hourglass"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Guinsoo's Rageblade (2600g)": "Recurve Bow → Guinsoo's",
                },
                "note": "Kraken + Rageblade = évolution Q rapide. Nashor's pour évoluer W.",
            },
            "vs tanks": {
                "ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Lord Dominik's Regards", "Nashor's Tooth", "Mortal Reminder"],
                "chemins": {},
                "note": "Lord Dom's + Kraken passif perce tous les tanks.",
            },
        },
        "counters": "Caitlyn (outrange), Draven (domine early), Miss Fortune (burst level 6)",
        "strong_vs": "Sivir, Ashe, Jinx (outmobile)",
        "tips": [
            "Évolue Q dès 100 bonus AD — c'est ton spike principal.",
            "Supercharge (E) avant d'engager pour le bonus AS.",
            "Void Seeker (W) pour sniper en sécurité ou finir les fuyards.",
            "Killer Instinct (R) : dash vers un allié qui cc l'ennemi.",
        ],
    },


    "Miss Fortune": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Lane bully, poke fort, ult devastateur en teamfight. Simple et efficace.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "lethality": {
                "ordre": ["Essence Reaver", "Youmuu's Ghostblade", "Lord Dominik's Regards", "Serylda's Grudge", "Serpent's Fang"],
                "chemins": {},
                "note": "Double Up (Q) + lethality = one-shot possible level 6.",
            },
            "crit": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {},
                "note": "Runaan's + Bullet Time (R) = teamfight devastating.",
            },
        },
        "counters": "Caitlyn (range), Ezreal (kite), Sivir (spell shield sur Q)",
        "strong_vs": "Jinx, Ashe, Kog'Maw (pas de mobilite)",
        "tips": [
            "Double Up (Q) : vise le minion derriere l'ennemi pour le toucher deux fois.",
            "Bullet Time (R) : canal interruptible — protege-toi avant de caster.",
            "Strut (passif) : conserve ton bonus MS en evitant les degats.",
        ],
    },

    "Vayne": {
        "role": "ADC (Bot Lane) / Top Lane",
        "playstyle": "Hypercarry late game anti-tank. Kite parfait, invisible avec R.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "on-hit": {
                "ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Wit's End", "Phantom Dancer", "Mortal Reminder"],
                "chemins": {},
                "note": "Silver Bolts (W) + Rageblade = % HP damage. Tue les tanks.",
            },
        },
        "counters": "Caitlyn (outrange), Draven (early), Miss Fortune",
        "strong_vs": "Tanks (Malphite, Ornn, Cho'Gath) — Silver Bolts ignore l'armure",
        "tips": [
            "Condemn (E) : stun en collant l'ennemi contre un mur.",
            "Final Hour (R) : invisibilite apres chaque Tumble (Q).",
            "Joue safe en early — tu scales en late.",
        ],
    },

    "Lucian": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Lane bully, high mobility, DPS burst. Fort en duo avec enchanteur.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Press the Attack (Precision)",
            "precision": "Presence of Mind | Legend: Alacrity | Cut Down",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "The Collector", "Lord Dominik's Regards", "Infinity Edge", "Guardian Angel"],
                "chemins": {},
                "note": "Press the Attack + double shot passif = burst rapide.",
            },
        },
        "counters": "Caitlyn (outrange), Jinx (late), Kog'Maw",
        "strong_vs": "Sivir, Ashe, Ezreal (early)",
        "tips": [
            "Chaque spell declenche le passif (double tir) — weave spells dans tes autos.",
            "Dash (E) apres chaque spell pour le cancel d'animation.",
            "Duo ideal : Nami, Senna, Lulu.",
        ],
    },

    "Xayah": {
        "role": "ADC (Bot Lane)",
        "playstyle": "DPS constant, invincible pendant R, synergique avec Rakan.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Alacrity | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards"],
                "chemins": {},
                "note": "Runaan's plante des feathers sur plusieurs cibles pour le recall (E).",
            },
        },
        "counters": "Caitlyn, Draven (early), Miss Fortune",
        "strong_vs": "Jinx, Ashe (pas de disengage)",
        "tips": [
            "Terminer par E pour ramasser les feathers — clean cuts passif.",
            "Bladecaller (E) : recall toutes les feathers = root si 3+.",
            "Featherstorm (R) : invincible + plante feathers sous les ennemis.",
        ],
    },

    "Sivir": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Waveclear, push rapide, MS buff equipe. Simple et efficace en ranked.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Coup de Grace",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {},
                "note": "Runaan's + Boomerang Blade (Q) = waveclear instantane.",
            },
        },
        "counters": "Caitlyn (outrange), Draven, Jinx (late)",
        "strong_vs": "Ezreal, Lux support (spell shield), Miss Fortune",
        "tips": [
            "Spell Shield (E) : bloque tout sort — save pour les cc dangereux.",
            "On the Hunt (R) : MS burst = parfait pour engage ou disengage.",
            "Q en bounce : vise entre deux ennemis pour toucher les deux.",
        ],
    },

    "Varus": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Poke, cc long-range, blight stacks. Polyvalent : lethality ou on-hit.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Alacrity | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Gathering Storm",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "lethality (poke)": {
                "ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Serpent's Fang", "Lord Dominik's Regards", "Edge of Night"],
                "chemins": {},
                "note": "Q charge + lethality = poke enorme. Fort en lane.",
            },
            "on-hit": {
                "ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Wit's End", "Mortal Reminder", "Runaan's Hurricane"],
                "chemins": {},
                "note": "Blight stacks (W) + on-hit = burst %HP.",
            },
        },
        "counters": "Draven, Lucian (early aggression)",
        "strong_vs": "Jinx, Sivir (outrange), Ashe",
        "tips": [
            "Hail of Arrows (E) : slow + Grievous Wounds. Utile vs healers.",
            "Chain of Corruption (R) : snare qui se propage — vise les groupes.",
            "Charge Q completement avant de tirer pour le max de degats.",
        ],
    },

    "Kog'Maw": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Hypercarry late game, range maximale, %HP damage. Necessite protection.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Alacrity | Cut Down",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "on-hit": {
                "ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Nashor's Tooth", "Wit's End", "Runaan's Hurricane"],
                "chemins": {},
                "note": "Bio-Arcane Barrage (W) + on-hit = DPS monstrueux sur tanks.",
            },
        },
        "counters": "Draven (early), Caitlyn, Lucian (mobilite)",
        "strong_vs": "Tous les tanks — W %HP damage",
        "tips": [
            "W actif : portee +130, %HP on-hit. Core de ton kit.",
            "Zero mobilite — joue avec un support qui peel (Lulu, Janna, Yuumi).",
            "Icathian Surprise (passif) : explose apres la mort. Bien positionner.",
        ],
    },

    "Twitch": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Invisible, sneak, teamfight devastatrice avec R. Fort en late.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Alacrity | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Phantom Dancer"],
                "chemins": {},
                "note": "Runaan's = spread poison + Spray and Pray (R) sur 5 ennemis.",
            },
        },
        "counters": "Caitlyn (range), Draven (early), Miss Fortune",
        "strong_vs": "Jinx, Ashe (peu de mobilite)",
        "tips": [
            "Ambush (Q) : invisible 1.25s, AS boost. Engage par derriere.",
            "Spray and Pray (R) : attaques traversent — file depuis le fond.",
            "Stack le poison (W) avant de declencher Contaminate (E).",
        ],
    },

    "Alistar": {
        "role": "Support",
        "playstyle": "Engage tank, combo W+Q = knock-up + push. Quasi invincible avec R.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Unflinching",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {
            "tank engage": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Knight's Vow", "Gargoyle Stoneplate"],
                "chemins": {},
                "note": "W+Q combo puis R pour absorber tout le burst ennemi.",
            },
        },
        "counters": "Blitzcrank (hook avant ton engage), Thresh, Nautilus",
        "strong_vs": "Lulu, Soraka, Nami (peu de mobilite face a l'engage)",
        "tips": [
            "Combo engage : W (headbutt) puis Q (pulverize) immediatement = knock-up garanti.",
            "Unbreakable Will (R) : -75% degats recus. Utilise quand tu es focus.",
            "Trample (E) : free stun sur la cible apres 5 charges.",
        ],
    },

    "Blitzcrank": {
        "role": "Support",
        "playstyle": "Hook = kill instantane. Tres impactful en lane, dangereux en bush.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Unflinching",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {
            "tank": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate"],
                "chemins": {},
                "note": "Full tank — tu n'as besoin que du hook pour carry.",
            },
        },
        "counters": "Thresh (lanterne), Morgana (spell shield), Sivir",
        "strong_vs": "Soraka, Sona, Lulu (pas de shield sur leur ADC)",
        "tips": [
            "Rocket Grab (Q) : hook en bush = surprise totale.",
            "Static Field (R) : silence AoE. Utilise en teamfight pour interrompre.",
            "Overheat (passif) : toutes les 7 autos = stun.",
        ],
    },

    "Braum": {
        "role": "Support",
        "playstyle": "Peel tank, shield directionnel, cc en chaine. Protection de l'ADC.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Unflinching",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {
            "tank peel": {
                "ordre": ["Locket of the Iron Solari", "Knight's Vow", "Warmog's Armor", "Zeke's Convergence", "Gargoyle Stoneplate"],
                "chemins": {},
                "note": "Colle ton ADC avec Knight's Vow — vous partagez les degats.",
            },
        },
        "counters": "Blitzcrank (hook), Thresh, Nautilus",
        "strong_vs": "Poke supports (Lux, Zyra) — tu bloques tout avec E",
        "tips": [
            "Stand Behind Me (W) : dash vers un allie = colle-toi pour peeler.",
            "Unbreakable (E) : face les projectiles pour les bloquer.",
            "Passive : 4 marks = stun. Laisse tes allies declencher les marks.",
        ],
    },

    "Janna": {
        "role": "Support",
        "playstyle": "Peel ultime, disengage, shielding. ADC survit grace a toi.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {
            "enchanteur": {
                "ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Ardent Censer", "Staff of Flowing Water", "Mikael's Blessing"],
                "chemins": {},
                "note": "Moonstone + Ardent Censer = ton ADC fait des degats enormes.",
            },
        },
        "counters": "Blitzcrank (hook before shield), Leona, Nautilus",
        "strong_vs": "Alistar, Blitzcrank (disengage leur engage avec R)",
        "tips": [
            "Monsoon (R) : repousse TOUS les ennemis. Utilise pour disengage.",
            "Eye of the Storm (E) : shield sur une tour — utile pour tenir un siege.",
            "Howling Gale (Q) : peut etre canalise longtemps pour plus de portee.",
        ],
    },

    "Sona": {
        "role": "Support",
        "playstyle": "Enchanteur, soins, MS, ultime global. Tres fort en duo coordonne.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {
            "enchanteur": {
                "ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Ardent Censer", "Staff of Flowing Water", "Redemption"],
                "chemins": {},
                "note": "Moonstone proc a chaque sort — heal passif permanent en fight.",
            },
        },
        "counters": "Blitzcrank, Nautilus, Leona (engage brutal)",
        "strong_vs": "Alistar, Braum (tes soins effacent leur engage)",
        "tips": [
            "Power Chord (passif) : toutes les 3 autos = effet bonus selon dernier sort.",
            "Crescendo (R) : AoE stun global. Coordonne avec ton ADC.",
            "Aria of Perseverance (W) : heal + armure. Priorite en trade.",
        ],
    },

    "Karma": {
        "role": "Support / Mid Lane",
        "playstyle": "Poke fort, shield avec MS, tres mobile. Domine early.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {
            "poke support": {
                "ordre": ["Shurelya's Battlesong", "Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff"],
                "chemins": {},
                "note": "Mantra + Q = burst enorme en poke ou en engage.",
            },
        },
        "counters": "Blitzcrank, Nautilus (engage avant que tu puisses shield)",
        "strong_vs": "Soraka, Sona (poke hors de portee)",
        "tips": [
            "Mantra (R) ameliore le prochain sort. Mantra+Q = gros degats.",
            "Mantra+E : shield + MS burst = pour fuir ou engager.",
            "Inspire (E) sans Mantra : shield simple mais rapide pour peeler.",
        ],
    },

    "Rakan": {
        "role": "Support",
        "playstyle": "Engage ultra-mobile, cc en chaine, synergique avec Xayah.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Gathering Storm",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R des que possible. W > E > Q.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {
            "enchanteur engage": {
                "ordre": ["Shurelya's Battlesong", "Locket of the Iron Solari", "Knight's Vow", "Zeke's Convergence", "Redemption"],
                "chemins": {},
                "note": "Shurelya's pour engager en flash — combo R+W sur plusieurs.",
            },
        },
        "counters": "Blitzcrank, Thresh, Nautilus",
        "strong_vs": "Soraka, Sona, Janna (enchanteurs sans mobilite)",
        "tips": [
            "Grand Entrance (W) : dash + knock-up. Core de ton engage.",
            "The Quickness (R) : charm = engage sur 3+ ennemis ideal.",
            "Gleaming Quill (Q) : heal si tu touches un champion — poke et soins.",
        ],
    },

    "Zilean": {
        "role": "Support",
        "playstyle": "Utilite massive, ralentissement, revive. Counter parfait des one-shot.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {
            "utilite": {
                "ordre": ["Shurelya's Battlesong", "Cosmic Drive", "Zhonya's Hourglass", "Rabadon's Deathcap", "Shadowflame"],
                "chemins": {},
                "note": "Cosmic Drive + Transcendence = CDR max pour R toujours dispo.",
            },
        },
        "counters": "Blitzcrank (hook avant que tu R), Nautilus",
        "strong_vs": "Toute equipe a assassin — R annule le one-shot",
        "tips": [
            "Double bombe (Q deux fois sur la meme cible) = stun.",
            "Chronoshift (R) : place sur l'ADC quand il engage ou quand il est focus.",
            "Time Warp (E) : ralentis l'ennemi qui engage, accelere l'allie qui fuit.",
        ],
    },

    "Renekton": {
        "role": "Top Lane",
        "playstyle": "Lane bully brutal, domine niveaux 1-9, snowball fort, tank-fighter.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "bruiser": {
                "ordre": ["Sundered Sky", "Black Cleaver", "Sterak's Gage", "Death's Dance", "Spirit Visage"],
                "chemins": {},
                "note": "Sundered Sky + Wrath (fury >50) = trade gagne a chaque fois.",
            },
        },
        "counters": "Jayce (poke range), Malphite (E bloc ton dash), Gnar",
        "strong_vs": "Sion, Nasus, Dr. Mundo, Mordekaiser (early)",
        "tips": [
            "Dominer niveaux 1-9 — tombe off tard game.",
            "Slice and Dice (E) double : entre avec E1, sort avec E2.",
            "Fury (passif) : a 50 fury, W = stun + double degats.",
        ],
    },

    "Jax": {
        "role": "Top Lane / Jungle",
        "playstyle": "1v1 le plus fort du jeu en late. Scale infiniment. Contre-pick universel.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "bruiser on-hit": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Wit's End", "Blade of the Ruined King", "Death's Dance"],
                "chemins": {},
                "note": "Trinforce Spellblade + Counter Strike (E) = burst DPS enorme.",
            },
        },
        "counters": "Teemo (blind), Quinn (poke), Gnar (range)",
        "strong_vs": "Tout en late — Jax 1v1 tout le monde apres Trinity + Sterak's",
        "tips": [
            "Counter Strike (E) : dodge toutes les autos pendant 2s, puis stun.",
            "Activate E apres le saut (Q) pour le combo complet.",
            "Passive : toutes les 3 autos = proc bonus degats.",
        ],
    },

    "Ornn": {
        "role": "Top Lane",
        "playstyle": "Tank engage massif, items craftes = avantage permanent pour l'equipe.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "full tank": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Thornmail", "Gargoyle Stoneplate", "Warmog's Armor"],
                "chemins": {},
                "note": "Heartsteel + Overgrowth = HP infinis. Immortel en late.",
            },
        },
        "counters": "Darius (burst avant ton engage), Illaoi (tentacles bloquent W)",
        "strong_vs": "Champions sans mobilite — Brittle (W passif) + R knock-up",
        "tips": [
            "Anvil Drop (W) : cree mur de forge + brittle. Core du kit.",
            "Call of the Forge God (R) : enorme portee — hit depuis loin.",
            "Craft items ameliores pour tes allies apres niveau 13.",
        ],
    },

    "Gnar": {
        "role": "Top Lane",
        "playstyle": "Split push (mini), teamfight (mega). Gestion de la rage = cle du champion.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Bone Plating | Overgrowth",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "bruiser tank": {
                "ordre": ["Trinity Force", "Heartsteel", "Sterak's Gage", "Frozen Heart", "Gargoyle Stoneplate"],
                "chemins": {},
                "note": "Trinity Force en premier pour le duel. Heartsteel pour les HP.",
            },
        },
        "counters": "Darius (si tu es en mini), Renekton, Irelia",
        "strong_vs": "Champions a portee melee — Mega Gnar throw les colle aux murs",
        "tips": [
            "GNAR! (R) : throw tout le monde quand ils sont contre un mur.",
            "Mini : kite et poke. Mega : engage et cc.",
            "Dump la rage dans les trades — transforme quand tout le monde est proche.",
        ],
    },

    "Dr. Mundo": {
        "role": "Top Lane / Jungle",
        "playstyle": "Tank regeneration absolue. Quasi immortel avec R en late. Farm et scale.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Second Wind | Overgrowth",
            "secondary_tree": "Sorcery",
            "secondary": "Transcendence | Gathering Storm",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "full tank": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Spirit Visage", "Warmog's Armor", "Thornmail"],
                "chemins": {},
                "note": "Spirit Visage amplifie le heal de R. Heartsteel = HP infinis.",
            },
        },
        "counters": "Darius (saigne), Garen (E reduit healing), Fiora (true damage)",
        "strong_vs": "Nasus, Cho'Gath, Malphite",
        "tips": [
            "Maximum Dosage (R) : sprint + heal massif. Utilise pour engage ou survive.",
            "Infected Bonesaw (Q) : range poke + Grievous Wounds.",
            "Heart Zapper (W) : tanke les degats puis restitue en HP.",
        ],
    },

    "Gangplank": {
        "role": "Top Lane",
        "playstyle": "Scale tres fort, degats globaux avec R, barils skill shot unique.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Bone Plating | Last Stand",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "crit": {
                "ordre": ["Trinity Force", "Essence Reaver", "Infinity Edge", "Lord Dominik's Regards", "Mortal Reminder"],
                "chemins": {},
                "note": "Sheen proc sur Q (Parrrley) = burst enorme a chaque Q.",
            },
        },
        "counters": "Darius (domine early), Renekton, Camille",
        "strong_vs": "Nasus, Malphite, champions immobiles",
        "tips": [
            "Powder Keg (E) : les barils s'enchainent — cree des triangles.",
            "Remove Scurvy (W) : cleanse TOUS les cc + heal.",
            "Cannon Barrage (R) : global. Utilise sur les teamfights partout sur la map.",
        ],
    },

    "Cho'Gath": {
        "role": "Top Lane / Support",
        "playstyle": "Scaling infini sur les HP avec R. Tank indestructible en late.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Second Wind | Overgrowth",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "full tank": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate"],
                "chemins": {},
                "note": "Chaque R stack augmente les HP max. Heartsteel amplifie.",
            },
        },
        "counters": "Darius, Renekton, Garen (early bully avant que tu stack)",
        "strong_vs": "Tanks immobiles — Rupture (Q) silence + knock-up",
        "tips": [
            "Feast (R) : execute → stack HP permanents. Priorite sur tout.",
            "Farm les monstres et minions avec R pour les stacks.",
            "Rupture (Q) : slow puis knock-up apres 0.5s — pre-vise.",
        ],
    },

    "Orianna": {
        "role": "Mid Lane",
        "playstyle": "Controle de zone avec la balle, shield, teamfight R devastateur.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "AP": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"],
                "chemins": {},
                "note": "Luden's pour waveclear. Zhonya's pour engager sans mourir.",
            },
        },
        "counters": "Fizz (dodge Q), Akali, Zed (gap close sur la balle)",
        "strong_vs": "Ahri, Viktor, Cassiopeia (teamfight R les annihile)",
        "tips": [
            "La balle reste sur le dernier allie — colle-toi a lui pour le shielder.",
            "Combo : E (balle vers allie) → allie engage → R pour pull tout le monde.",
            "Command: Attack (Q) : poke constant — vise entre minions et ennemi.",
        ],
    },

    "Twisted Fate": {
        "role": "Mid Lane",
        "playstyle": "Roam global avec R, poke/cc avec Gold Card, simple mais impactant.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Gathering Storm",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "AP roam": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Lich Bane", "Rabadon's Deathcap", "Void Staff"],
                "chemins": {},
                "note": "Lich Bane proc sur Gold Card stun = burst instantane en roam.",
            },
        },
        "counters": "Zed, Talon, LeBlanc (mobilite pour esquiver tes Q)",
        "strong_vs": "Ryze, Viktor, Orianna (tu roam pendant qu'ils farmnet)",
        "tips": [
            "Pick a Card (W) : Gold Card (jaune) = stun. Pratique en roam.",
            "Destiny (R) : vision globale + portal. Roam apres chaque push.",
        ],
    },

    "Vex": {
        "role": "Mid Lane",
        "playstyle": "Mage anti-mobilite. Counter direct des champions dash. Forte en teamfight.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Gathering Storm",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "AP": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"],
                "chemins": {},
                "note": "Personal Space (E) + Fear Beyond Death (R) reset = snowball rapide.",
            },
        },
        "counters": "Fizz (dive), Zed (burst avant fear), Katarina",
        "strong_vs": "Yasuo, Akali, Sylas, Ekko (tous les champions a dash)",
        "tips": [
            "Doom (passif) : charge quand un ennemi dash. Next W = fear.",
            "Shadow Surge (R) : one-shot + reset si tu tues la cible.",
        ],
    },

    "Fizz": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Assassin mobile, untargetable avec E, one-shot avec combo.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "burst": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Lich Bane", "Rabadon's Deathcap", "Zhonya's Hourglass"],
                "chemins": {},
                "note": "Lich Bane proc sur Q apres E = burst instantane.",
            },
        },
        "counters": "Lissandra (R immune), Galio, Malzahar (R cancel E)",
        "strong_vs": "Yasuo, Katarina, Ahri (tu untarget tout leur cc avec E)",
        "tips": [
            "Playful/Trickster (E) : invincible pendant 0.75s — dodge tout skill.",
            "Combo : R (requin) → E → Q → W (auto-weave) → Ignite.",
        ],
    },

    "Talon": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Assassin, roam rapide, one-shot et fuite par les murs.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {
            "lethality": {
                "ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards"],
                "chemins": {},
                "note": "Lethality max = ADC/support one-shot apres niveau 6.",
            },
        },
        "counters": "Lissandra (root), Malzahar (R cancel), Galio",
        "strong_vs": "Ahri, Viktor, Orianna (immobiles face au burst)",
        "tips": [
            "Roam par les murs (E) — faster que les autres.",
            "Combo : E (leap) → W (blades) → Q (auto) → R (invisibilite) → retour.",
        ],
    },

    "LeBlanc": {
        "role": "Mid Lane",
        "playstyle": "One-shot burst instantane, faux jumeau, impossible a punir si bien joue.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "burst": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"],
                "chemins": {},
                "note": "Q marque → R(Q) double mark = one-shot instantane.",
            },
        },
        "counters": "Lissandra, Galio, Malzahar",
        "strong_vs": "Ahri, Syndra, Orianna",
        "tips": [
            "Combo : Q → W (dash) → E (root) → RQ (double marque) → Ignite.",
            "Distortion (W) : dash puis retour a la position — utilise pour escape.",
        ],
    },

    "Malzahar": {
        "role": "Mid Lane",
        "playstyle": "Hard CC avec R, push rapide, silences. Fort contre les assassins.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Gathering Storm",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {
            "AP": {
                "ordre": ["Luden's Tempest", "Liandry's Anguish", "Rabadon's Deathcap", "Shadowflame", "Void Staff"],
                "chemins": {},
                "note": "Liandry's + Malefic Visions (E) = DoT massif sur tanks.",
            },
        },
        "counters": "Zed (QSS cancel R), Kassadin, Fizz (dodge R avec E)",
        "strong_vs": "Talon, LeBlanc, Qiyana (Void Shield block leur burst)",
        "tips": [
            "Void Shield (passif) : absorbe un spell. Recharge quand tu n'es pas hit.",
            "Nether Grasp (R) : suppress 2.5s — utilise sur le carry.",
            "Malefic Visions (E) : propagation aux minions — waveclear rapide.",
        ],
    },

    "Rengar": {
        "role": "Jungle / Top Lane",
        "playstyle": "Assassin embusque, one-shot depuis l'invisibilite. Snowball fort.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Hail of Blades (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Precision",
            "secondary": "Triumph | Last Stand",
        },
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {
            "lethality": {
                "ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards"],
                "chemins": {},
                "note": "Stack 4 ferocity → Q empowered = one-shot instantane.",
            },
        },
        "counters": "Lee Sin (duel), Xin Zhao, Graves",
        "strong_vs": "ADC, supports, cibles seules hors de vision",
        "tips": [
            "Ferocity : 4 stacks = Q renforce. Stack en jungle avant le gank.",
            "Thrill of the Hunt (R) : invisibilite + vision des ennemis. Track l'ADC.",
            "Combo : R (invis) → E (debuff armor) → Q empowered → burst.",
        ],
    },

    "Evelynn": {
        "role": "Jungle",
        "playstyle": "Assassin invisible permanente apres niveau 6. Gank toutes les lanes.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {
            "AP burst": {
                "ordre": ["Riftmaker", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"],
                "chemins": {},
                "note": "Last Caress (R) fait 200%+ degats sous 30% HP.",
            },
        },
        "counters": "Lee Sin (ward + reveal), Graves, Kindred",
        "strong_vs": "ADC isole, support, mid sans ward",
        "tips": [
            "Camouflage (passif) : invisible a partir du niveau 6 hors combat.",
            "Allure (W) : charm si stacked sur la cible avant d'attaquer.",
            "Last Caress (R) : execute sous 30% HP.",
        ],
    },

    "Xin Zhao": {
        "role": "Jungle",
        "playstyle": "Engage brutal, knock-up, resistance avec R. Simple et efficace.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {
            "bruiser": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Black Cleaver", "Death's Dance", "Guardian Angel"],
                "chemins": {},
                "note": "Trinity Force + Crescent Guard (Q) = burst + sustain fight.",
            },
        },
        "counters": "Rammus (counter engage), Lee Sin, Graves",
        "strong_vs": "ADC, mid sans gap close, champions immobiles",
        "tips": [
            "Audacious Charge (E) : dash + slow. Always-on engage.",
            "Crescent Guard (Q) : 3e attaque = knock-up. Weave avec des autos.",
            "Crescent Sweep (R) : repousse tout sauf ceux dans le cone.",
        ],
    },

    "Rammus": {
        "role": "Jungle",
        "playstyle": "Tank ultra-mobile avec Powerball, counter des equipes AD.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Conditioning | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {
            "full tank": {
                "ordre": ["Sunfire Aegis", "Thornmail", "Warmog's Armor", "Gargoyle Stoneplate", "Abyssal Mask"],
                "chemins": {},
                "note": "Thornmail + Defensive Ball Curl (W) = les AD se tuent sur toi.",
            },
        },
        "counters": "AP heavy teams, Kha'Zix",
        "strong_vs": "Toute equipe AD lourde — passif renvoie l'armure en degats",
        "tips": [
            "Powerball (Q) : plus tu roules longtemps, plus c'est fort.",
            "Defensive Ball Curl (W) : armor massive + return damage.",
        ],
    },

    "Zac": {
        "role": "Jungle",
        "playstyle": "Engage sur toute la map, cc en chaine, tres resilient grace aux blobs.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Conditioning | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {
            "tank": {
                "ordre": ["Sunfire Aegis", "Heartsteel", "Warmog's Armor", "Thornmail", "Abyssal Mask"],
                "chemins": {},
                "note": "Heartsteel + blobs passif HP restore = quasi immortel.",
            },
        },
        "counters": "Lee Sin, Xin Zhao (duel early), Rengar",
        "strong_vs": "Champions groupes — Let's Bounce (R) = knock-up repete",
        "tips": [
            "Elastic Slingshot (E) : range gigantesque. Engage depuis la riviere.",
            "Let's Bounce (R) : plus longtemps = plus de bounce = plus de knock-up.",
            "Passive (blobs) : ramasse les blobs pour te soigner.",
        ],
    },

    "Viego": {
        "role": "Jungle",
        "playstyle": "Possede les ennemis tues, snowball rapide. Chaos total.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {
            "bruiser": {
                "ordre": ["Kraken Slayer", "Blade of the Ruined King", "Sterak's Gage", "Death's Dance", "Guardian Angel"],
                "chemins": {},
                "note": "BotRK + possession passif = tu seras a pleine vie apres chaque kill.",
            },
        },
        "counters": "Rammus, Lee Sin, Graves",
        "strong_vs": "Teamfights — tu possedes l'ennemi tue et continues le fight",
        "tips": [
            "Sovereign's Domination (passif) : possede l'ennemi 10s apres kill.",
            "Heartbreaker (R) : dash. Combo dans la possession = reset.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CHAMPIONS MANQUANTS — AJOUT COMPLET
    # ══════════════════════════════════════════════════════════════════════════

    "Akshan": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Assassin mobile, revive les allies, grappin sur les murs. Unique.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Cut Down", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"crit": {"ordre": ["Kraken Slayer", "Galeforce", "Infinity Edge", "Lord Dominik's Regards", "Guardian Angel"], "chemins": {}, "note": "Galeforce + grappin (E) = mobilite extreme."}},
        "counters": "Zed, Talon, Qiyana",
        "strong_vs": "Champions immobiles — grappin permet de contourner",
        "tips": ["Grappin (E) : accroche un mur et tourne autour infiniment.", "Comeuppance (R) : charge = plus de degats. Utilise hors combat.", "Revive passif : tue l'assassin de ton allie pour le reviver."],
    },

    "Anivia": {
        "role": "Mid Lane",
        "playstyle": "Mage control, mur de glace, DPS passif avec R. Tres forte en teamfight.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Rod of Ages", "Luden's Tempest", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Rod of Ages pour la mana et le sustain. R permanent en teamfight."}},
        "counters": "Fizz, Zed, LeBlanc (mobilite evite le mur)",
        "strong_vs": "Champions immobiles — Crystallize (W) coupe les fuites",
        "tips": ["Crystallize (W) : mur de glace = coupe les echappatoires.", "Glacial Storm (R) : toggle AoE — laisse actif en teamfight.", "Rebirth (passif) : oeuf apres la mort. Ne meurs pas sous la tour ennemie."],
    },

    "Annie": {
        "role": "Mid Lane / Support",
        "playstyle": "Burst AP simple, stun avec Tibbers (R) ou 4 sorts. Parfaite pour apprendre.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"burst": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "4 sorts stackes → stun → Tibbers (R) = combo one-shot."}},
        "counters": "Fizz (dodge), Zed, LeBlanc",
        "strong_vs": "Champions immobiles — stun garanti avec 4 stacks",
        "tips": ["Compte tes stacks (passif) : 4 = prochain sort stun.", "Tibbers (R) : AoE + ours qui brule. Engage en equipe.", "Incinerate (W) : AoE — utile pour stacker ou waveclear."],
    },

    "Aphelios": {
        "role": "ADC (Bot Lane)",
        "playstyle": "5 armes = 5 kits. Le plus complexe du jeu. Tres haut plafond.",
        "summoner_spells": "Flash + Heal",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Presence of Mind | Legend: Bloodline | Cut Down", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Rotation d'armes — pas d'ordre fixe.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"standard": {"ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Bloodthirster"], "chemins": {}, "note": "Runaan's est core — Calibrum + Hurricane = snipe multi-cibles."}},
        "counters": "Draven (early), Caitlyn, Lucian",
        "strong_vs": "Jinx, Ashe, Sivir",
        "tips": ["Calibrum (fusil) : poke + marque.", "Crescendum (chakram) : DPS melee.", "Infernum (flamethrower) : AoE, meilleur avec Runaan's.", "Severum (faucille) : heal, survie en fight."],
    },

    "Aurora": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Mage assassin mobile, saute dans le Void, burst et fuite. Champion recent.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"burst AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "Burst rapide + mobilite du R pour fuir apres."}},
        "counters": "Zed, Talon, Fizz",
        "strong_vs": "Champions immobiles en lane",
        "tips": ["Beyond the Veil (R) : entre dans le Void — repositionne ou engage.", "Combo : Q → E → W → R pour le burst complet.", "Passive : bonus degats apres sortie du Void."],
    },

    "Azir": {
        "role": "Mid Lane",
        "playstyle": "Mage control, soldats qui attaquent, poke safe. Haut skill cap.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Nashor's Tooth", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Nashor's + soldats = DPS passif enorme. Safe poke constant."}},
        "counters": "Zed, Talon, LeBlanc (gap close sur tes soldats)",
        "strong_vs": "Orianna, Lissandra, Syndra (poke safe hors de portee)",
        "tips": ["Soldiers : place W → Q pour les faire attaquer. Core du kit.", "Emperor's Divide (R) : mur de soldats = disengage ou engage.", "Shifting Sands (E) : dash vers le soldat + knock-up."],
    },

    "Bard": {
        "role": "Support",
        "playstyle": "Utilitaire unique, collecte les chimes, portails, ultime global qui gele.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"enchanteur": {"ordre": ["Shurelya's Battlesong", "Locket of the Iron Solari", "Zeke's Convergence", "Redemption", "Knight's Vow"], "chemins": {}, "note": "Collecte les chimes entre les combats pour les stacks passifs."}},
        "counters": "Blitzcrank, Nautilus (tu es souvent en roam)",
        "strong_vs": "Supports immobiles — portails et stun impredictibles",
        "tips": ["Cosmic Binding (Q) : stun si touche deux ennemis ou un ennemi + mur.", "Magical Journey (E) : portail traversable par les allies.", "Tempered Fate (R) : gele TOUT dans la zone. Allie ou ennemi."],
    },

    "Bel'Veth": {
        "role": "Jungle",
        "playstyle": "DPS on-hit, infini d'autos apres des kills, transformation post-Baron.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"on-hit": {"ordre": ["Kraken Slayer", "Blade of the Ruined King", "Guinsoo's Rageblade", "Wit's End", "Mortal Reminder"], "chemins": {}, "note": "Stacks apres kills = AS infini. Rageblade amplifie les on-hit."}},
        "counters": "Lee Sin, Graves, Xin Zhao (duel early)",
        "strong_vs": "Champions fragiles — tu les debordent avec les autos rapides",
        "tips": ["Royal Maelstrom (E) : canal qui absorbe les degats = sustain en fight.", "Endless Banquet (passif) : chaque kill donne un stack AS permanent.", "True Form (R) : transformation apres baron — forme plus puissante."],
    },

    "Brand": {
        "role": "Support / Mid Lane",
        "playstyle": "Poke AP, rebonds sur les flammes, teamfight devastateur. Dangereux.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Passive Blaze : 3 sorts = stun + explosion. Bounce R = devastateur en teamfight."}},
        "counters": "Blitzcrank, Nautilus, Morgana (shield absorbe ton combo)",
        "strong_vs": "Champions groupes — R rebondit sur tout le monde",
        "tips": ["Blaze (passif) : 3 sorts sur la meme cible = explosion AoE.", "Pillar of Flame (W) : double degats si la cible est en feu.", "Pyroclasm (R) : rebondit entre ennemis. Lance quand ils sont groupes."],
    },

    "Briar": {
        "role": "Jungle / Top Lane",
        "playstyle": "Assassin bestial, frenetique, saigne constamment, forte en duel.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Sundered Sky", "Sterak's Gage", "Black Cleaver", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Sundered Sky + saignement passif = sustain enorme en duel."}},
        "counters": "Rammus, Lee Sin (kite ta frenetique)",
        "strong_vs": "Champions immobiles — tu ne peux pas tirer mais tu deals enorme",
        "tips": ["Pas de retour en arriere — une fois engage, commit a fond.", "Headrush (E) : dive + knock-up. Engage core.", "Palisade of Pain (R) : global, te lance sur la cible. Utilise pour finisher."],
    },

    "Cassiopeia": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "DPS AP continu, empoisonnement, ult petrification. Scale enormement.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP DPS": {"ordre": ["Rod of Ages", "Liandry's Anguish", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Rod of Ages + mana = spam de E illimite. DPS AP le plus haut du jeu."}},
        "counters": "Zed, Talon, LeBlanc (burst avant ton DPS)",
        "strong_vs": "Champions immobiles — poison permanent et kite",
        "tips": ["Twin Fang (E) : 0.5s CD si la cible est empoisonnee. Spam infini.", "Petrifying Gaze (R) : regarde l'ennemi = petrification. Dos = slow.", "Miasma (W) : zone poison + no dash. Force l'ennemi a rester empoisonne."],
    },

    "Corki": {
        "role": "Mid Lane",
        "playstyle": "ADC en mid, hybride AD/AP, packages tous les 4 min = engage global.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"hybride": {"ordre": ["Trinity Force", "Manamune", "The Collector", "Lord Dominik's Regards", "Rabadon's Deathcap"], "chemins": {}, "note": "Trinity Force spike. Manamune pour le mana. Hybride AD/AP."}},
        "counters": "Zed, Talon, Fizz (gap close sur toi)",
        "strong_vs": "Orianna, Viktor, Azir (poke safe avec Phosphorus Bomb)",
        "tips": ["The Package : engage global toutes les 4 min. Gros power spike.", "Missiles (R) : poke constant — utilise entre les autos.", "Gatling Gun (E) : reduit armure + MR — engage en fight."],
    },

    "Diana": {
        "role": "Mid Lane / Jungle",
        "playstyle": "Dive assassin AP, reset de dash apres moonlight, burst fort niveau 6.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Cheap Shot | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"burst AP": {"ordre": ["Luden's Tempest", "Lich Bane", "Shadowflame", "Rabadon's Deathcap", "Void Staff"], "chemins": {}, "note": "Lich Bane proc sur W apres Q = burst instantane."}},
        "counters": "Lissandra (R immune), Galio, Malzahar",
        "strong_vs": "Ahri, Orianna, Syndra (dive les one-shot)",
        "tips": ["Combo : Q (moonlight) → R (pull) → W → Q reset R → deuxieme dash.", "Moonsilver Blade (passif) : toutes les 3 autos = AoE splash.", "Pale Cascade (W) : shield avant le burst — important pour survive."],
    },

    "Elise": {
        "role": "Jungle",
        "playstyle": "Gank early, cocoon = cc long, deux formes. Difficile mais recompensante.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Cheap Shot | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "Cocoon (E human) → Rappel (descend araignee) → burst complet."}},
        "counters": "Lee Sin (duel), Graves, Xin Zhao",
        "strong_vs": "Squishies sans dash",
        "tips": ["Volatile Spiderling (W human) : slow + degats.", "Cocoon (E human) : stun. Core du gank.", "Rappel (E araignee) : invincible 2s. Evite le burst ou les tours."],
    },

    "Fiddlesticks": {
        "role": "Jungle",
        "playstyle": "Jumpscare depuis les bushes, teamfight R apocalyptique.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Dark Harvest (Domination)", "domination": "Cheap Shot | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Transcendence | Gathering Storm"},
        "skill_order": "R des que possible. W > E > Q.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"AP AoE": {"ordre": ["Liandry's Anguish", "Zhonya's Hourglass", "Rabadon's Deathcap", "Void Staff", "Shadowflame"], "chemins": {}, "note": "Crowstorm (R) + Zhonya's = engage sans risque de burst."}},
        "counters": "Lee Sin (ward), Graves, Rengar",
        "strong_vs": "Champions groupes — R AoE devaste les teamfights",
        "tips": ["Crowstorm (R) : canal en bush → apparait au milieu des ennemis.", "Effigy (passif) : laisse un faux Fiddle — bluff les ganks.", "Bountiful Harvest (W) : drain canal = heal massif si ennemis ne bougent pas."],
    },

    "Galio": {
        "role": "Mid Lane / Support",
        "playstyle": "Tank engage global avec R, anti-mage, tres fort si ennemi AP.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Bone Plating | Unflinching", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"tank AP": {"ordre": ["Luden's Tempest", "Zhonya's Hourglass", "Shadowflame", "Rabadon's Deathcap", "Void Staff"], "chemins": {}, "note": "Hero's Entrance (R) : atterrit sur un allie partout sur la map."}},
        "counters": "Zed, Talon (AD bypass ton magic resist)",
        "strong_vs": "Kassadin, Viktor, Ahri, toute equipe AP lourde",
        "tips": ["Hero's Entrance (R) : global engage — utilise quand un allie engage.", "Justice Punch (E) : dash + knock-up. Core du combo.", "Winds of War (Q) : tornade reste sur place — pose devant eux."],
    },

    "Gragas": {
        "role": "Jungle / Top Lane / Mid Lane",
        "playstyle": "Tank AP polyvalent, R qui deplace les ennemis au choix. Tres utile.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Bone Plating | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"tank AP": {"ordre": ["Sunfire Aegis", "Warmog's Armor", "Zhonya's Hourglass", "Abyssal Mask", "Gargoyle Stoneplate"], "chemins": {}, "note": "R (Explosive Cask) deplace les ennemis — envoie-les vers tes allies."}},
        "counters": "Lee Sin, Graves, Xin Zhao",
        "strong_vs": "Champions groupes — R separe ou regroupe selon le besoin",
        "tips": ["Explosive Cask (R) : force le deplacement. Envoie l'ADC vers ton equipe.", "Body Slam (E) : dash + slow. Engage ou escape.", "Happy Hour (passif) : heal apres chaque sort — sustain en jungle."],
    },

    "Gwen": {
        "role": "Top Lane / Jungle",
        "playstyle": "Fighter AP, zone d'innocence intouchable, DPS fort vs tanks.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Overgrowth"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"AP fighter": {"ordre": ["Riftmaker", "Nashor's Tooth", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "Riftmaker + true damage passif = devastatrice vs tanks. Nashor's pour l'AS."}},
        "counters": "Darius, Renekton, Camille (early bully avant powerspike)",
        "strong_vs": "Tanks — Q true damage % HP. Countre Malphite, Ornn.",
        "tips": ["Hallowed Mist (W) : zone intouchable pour les ennemis exterieurs — reste dedans.", "Snip Snip! (Q) : plus tu charges, plus tu couses. Termine par le centre.", "Skip 'n Slash (E) : dash + AS. Engage puis spam Q."],
    },

    "Heimerdinger": {
        "role": "Mid Lane / Support / Top Lane",
        "playstyle": "Tourelles qui bombardent, tres fort en siege et en defense.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "3 tourelles dans la zone + E stun = damage enorme."}},
        "counters": "Zed, Talon, Fizz (dive les tourelles)",
        "strong_vs": "Champions immobiles qui restent en lane",
        "tips": ["Place max 3 tourelles (Q) — elles s'ameliorent quand tu en places plus.", "UPGRADE!!! (R) + W = mega roquette = burst enorme.", "Electro-Grenade (E) : stun AoE si touche une tourelle."],
    },

    "Illaoi": {
        "role": "Top Lane",
        "playstyle": "Pression split push, tentacules qui soignent, inarretable avec R.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Grasp of the Undying (Resolve)", "resolve": "Demolish | Bone Plating | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"bruiser": {"ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Sterak's Gage", "Thornmail"], "chemins": {}, "note": "Heartsteel + soins tentacules (Q) = quasi impossible a tuer en late."}},
        "counters": "Darius (burst avant que tu heales), Fiora, Camille",
        "strong_vs": "Champions immobiles — tentacules punissent les fights prolonges",
        "tips": ["Harsh Lesson (W) : dash sur tentacule = repositionnement.", "Test of Spirit (E) : sort l'ame de l'ennemi. Tue l'ame = tentacule bonus.", "Leap of Faith (R) : invoque des tentacules. Reste dans la zone."],
    },

    "Ivern": {
        "role": "Jungle",
        "playstyle": "Jungler pacifiste, libere les camps au lieu de les tuer, enchanteur.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Summon Aery (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Resolve", "secondary": "Font of Life | Revitalize"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + Refillable Potion",
        "build_paths": {"enchanteur": {"ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Ardent Censer", "Staff of Flowing Water", "Redemption"], "chemins": {}, "note": "Daisy (R) engage pour toi. Toi tu shield et peel."}},
        "counters": "Lee Sin, Graves (duel — tu ne peux pas combattre)",
        "strong_vs": "Champions fragiles que Daisy (R) peut distraire",
        "tips": ["Rootcaller (Q) : root longue duree — gank asure.", "Brushmaker (W) : buissons partout — vision et engagement safe.", "Daisy (R) : tank IA qui engage pour toi."],
    },

    "Jarvan IV": {
        "role": "Jungle / Top Lane",
        "playstyle": "Engage avec E+Q combo, cage, tank fighter. Fort et simple.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Black Cleaver", "Sterak's Gage", "Death's Dance", "Spirit Visage"], "chemins": {}, "note": "E+Q combo = knock-up garanti. Cataclysm (R) isole le carry."}},
        "counters": "Lee Sin (duel), Graves, Xin Zhao",
        "strong_vs": "ADC isole, champions sans dash pour echapper au R",
        "tips": ["Combo engage : E (standard) → Q (Dragon Strike) = knock-up instantane.", "Cataclysm (R) : cage autour d'une cible. Isole le carry.", "Demacian Standard (E) : place en avant, puis Q pour traverser."],
    },

    "Kayle": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Hypercarry late, evolue en 3 phases. Fragile early, invincible niveau 16.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Presence of Mind | Legend: Alacrity | Cut Down", "secondary_tree": "Resolve", "secondary": "Second Wind | Overgrowth"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"AP crit": {"ordre": ["Nashor's Tooth", "Kraken Slayer", "Rabadon's Deathcap", "Void Staff", "Infinity Edge"], "chemins": {}, "note": "Nashor's + evolution niveau 11 = DPS AP/AS devastateur."}},
        "counters": "Darius, Renekton, Camille (domine early avant evolution)",
        "strong_vs": "Tout le monde en late niveau 16 — invincible avec R + AS max",
        "tips": ["Survive les niveaux 1-10. Farm et scale.", "Niveau 6 : attaques a portee. Niveau 11 : AoE. Niveau 16 : attaques de feu.", "Divine Judgment (R) : invincibilite 2.5s. Sur toi ou un allie."],
    },

    "Kennen": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Range AP, stun avec energie, teamfight R AoE. Counter les melee.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"AP": {"ordre": ["Hextech Rocketbelt", "Nashor's Tooth", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Rocketbelt pour l'engage. R + Zhonya's = engage sans mourir."}},
        "counters": "Darius (si tu approches), Vladimir (sustain absorbe ton poke)",
        "strong_vs": "Champions melee — kite et poke avec Q constant",
        "tips": ["3 marks (passif) : stun. Applique avec Q, W actif, ou R.", "Lightning Rush (E) : invincible brievement + vitesse. Engage ou escape.", "Slicing Maelstrom (R) : AoE stun avec Zhonya's = teamfight win."],
    },

    "Kindred": {
        "role": "Jungle",
        "playstyle": "Marque les ennemis pour les tuer, R = invincibilite equipe.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Press the Attack (Precision)", "precision": "Triumph | Legend: Alacrity | Cut Down", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"crit on-hit": {"ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Lord Dominik's Regards", "Mortal Reminder", "Phantom Dancer"], "chemins": {}, "note": "Chaque stack marque = bonus degats passifs sur autos."}},
        "counters": "Lee Sin, Graves, Xin Zhao (duel early)",
        "strong_vs": "Dr. Mundo, Aatrox, Tryndamere (Kindred's R annule leur R)",
        "tips": ["Lamb's Respite (R) : tout le monde dans la zone est invincible 4s.", "Marque les ennemis en jungle pour accumuler les stacks.", "Wolf's Frenzy (W) : cree zone de loot. Farm dedans."],
    },

    "Kled": {
        "role": "Top Lane",
        "playstyle": "Duel agressif, impossible a fuir avec R, deux barres de vie.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"bruiser": {"ordre": ["Sundered Sky", "Black Cleaver", "Sterak's Gage", "Death's Dance", "Maw of Malmortius"], "chemins": {}, "note": "Sundered Sky proc sur Q (Beartrap) = burst fort."}},
        "counters": "Darius (saigne meme demonte), Fiora, Camille",
        "strong_vs": "Champions immobiles — Chaaaaarge!!! (R) impossible a fuir",
        "tips": ["Demontage et remontage : gere ton courage (barre jaune).", "Chaaaaarge!!! (R) : engage depuis loin + courage a l'equipe.", "Jousting (E) : double dash — utilise pour reset autos."],
    },

    "Lillia": {
        "role": "Jungle",
        "playstyle": "Clear rapide, degats passifs AoE, endort l'equipe ennemie avec R.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"AP": {"ordre": ["Liandry's Anguish", "Demonic Embrace", "Rylai's Crystal Scepter", "Shadowflame", "Rabadon's Deathcap"], "chemins": {}, "note": "Rylai's + passive DoT = kite permanent."}},
        "counters": "Lee Sin, Graves, Xin Zhao",
        "strong_vs": "Champions groupes — Lilting Lullaby (R) endort toute l'equipe",
        "tips": ["Dream Dust (passif) : DoT magique sur toutes les autos.", "Lilting Lullaby (R) : endort les ennemis qui ont du Drowsy (W stack).", "Blooming Blows (Q) : hit le bord exterieur pour les vrais degats."],
    },

    "Lissandra": {
        "role": "Mid Lane",
        "playstyle": "Mage control, cc en chaine, R = engage ou survivre.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Bone Plating | Overgrowth", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP control": {"ordre": ["Luden's Tempest", "Zhonya's Hourglass", "Shadowflame", "Rabadon's Deathcap", "Void Staff"], "chemins": {}, "note": "Zhonya's pour utiliser R agressivement — engage + hourglass."}},
        "counters": "Zed (R neutre face au mark), LeBlanc, Fizz",
        "strong_vs": "Katarina, Kassadin, Talon (cc les stoppe totalement)",
        "tips": ["Frozen Tomb (R) : sur toi-meme = survivre le burst. Sur ennemi = engager.", "Ring of Frost (W) : root — combo avec E (dash dessus).", "Combo engage : E → W → Q → R."],
    },

    "Maokai": {
        "role": "Support / Top Lane / Jungle",
        "playstyle": "Tank CC, sapling qui poke, R AoE ralentissement. Tres resilient.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Bone Plating | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {"tank": {"ordre": ["Locket of the Iron Solari", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate", "Abyssal Mask"], "chemins": {}, "note": "Sapling Toss (E) dans les buissons = poke massif. R zone slow permanent."}},
        "counters": "Blitzcrank, Nautilus, Thresh",
        "strong_vs": "Champions qui se groupent — R ralentit tout le monde",
        "tips": ["Nature's Grasp (R) : grande zone qui ralentit et root. Teamfight win.", "Sapling Toss (E) : dans un buisson = double degats.", "Twisted Advance (W) : root. Engage principal."],
    },

    "Master Yi": {
        "role": "Jungle",
        "playstyle": "Hypercarry late, reset de dash apres chaque kill, untargetable avec Q.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Sudden Impact | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"on-hit": {"ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Wit's End", "Blade of the Ruined King", "Mortal Reminder"], "chemins": {}, "note": "Alpha Strike (Q) puis Highlander (R) = inarretable en teamfight."}},
        "counters": "Rammus (thornmail), Lee Sin (blind), Rengar (burst instant)",
        "strong_vs": "Squishies isoles, ADC sans peel, junglers gank-dependants",
        "tips": ["Alpha Strike (Q) : invincible pendant. Dodge les cc.", "Highlander (R) : AS + MS + ignores slows. Reset apres kill.", "Wuju Style (E) : true damage actif. Utilise dans le burst."],
    },

    "Naafiri": {
        "role": "Mid Lane",
        "playstyle": "Assassin simple avec meute de dahkabs, engage en pack. Accessible.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards"], "chemins": {}, "note": "Q en poke + lethality = burst fort. Meute renforcee."}},
        "counters": "Lissandra, Galio, Malzahar",
        "strong_vs": "ADC isoles, supports",
        "tips": ["Pack Hunt (R) : engage + meute renforcee. Engage principal.", "Hounds' Pursuit (W) : root si deux dahkabs touchent.", "Mange des minions pour reconstituer les dahkabs."],
    },

    "Neeko": {
        "role": "Mid Lane / Support",
        "playstyle": "Poke, deguisement, ult AoE surprise. Forte en teamfight.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP burst": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Pop Blossom (R) + Zhonya's = engage sans risque."}},
        "counters": "Zed, Fizz, Talon",
        "strong_vs": "Orianna, Syndra, Lux",
        "tips": ["Inherent Glamour (passif) : deguise-toi en allie pour surprendre.", "Pop Blossom (R) : invisible pendant charge → knock-up AoE. Engage en bush.", "Blooming Burst (Q) : rebondit sur les ennemis proches."],
    },

    "Nidalee": {
        "role": "Jungle",
        "playstyle": "Poke skill shot, clear rapide, gank avec traps. Haut skill cap.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Dark Harvest (Domination)", "domination": "Cheap Shot | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q (cougar) > W > E.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Spear (Q humaine) apres trap (W) = degats x2."}},
        "counters": "Lee Sin (duel), Xin Zhao, Graves",
        "strong_vs": "Squishies = spear one-shot level 6+",
        "tips": ["Javelin Toss (Q) : plus c'est loin, plus ca fait mal.", "Bushwhack (W) : place trap → ennemis debuffes = spear double degats.", "Cougar form (R) : heal + dps dans les camps."],
    },

    "Nilah": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Melee ADC, forte en duel, synergique avec les enchanteurs.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Overgrowth"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"standard": {"ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Blade of the Ruined King", "Wit's End", "Phantom Dancer"], "chemins": {}, "note": "Melee = auto-attacks rapides. Rageblade + on-hit core."}},
        "counters": "Caitlyn (outrange), Jinx, Kog'Maw",
        "strong_vs": "Sivir, Ashe, champions sans mobilite",
        "tips": ["Slipstream (E) : dash a travers les ennemis = engager ou fuir.", "Apotheosis (R) : AoE, attire les ennemis, partage les soins avec allies.", "Joue avec un support qui engage (Nautilus, Thresh)."],
    },

    "Nocturne": {
        "role": "Jungle",
        "playstyle": "Gank global avec R, assassin de cibles isolees, coupe la vision.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Hail of Blades (Domination)", "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter", "secondary_tree": "Precision", "secondary": "Triumph | Last Stand"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Guardian Angel"], "chemins": {}, "note": "Dusk Bringer (R) global — flanque depuis nimporte ou."}},
        "counters": "Lee Sin (duel), Graves, Rammus",
        "strong_vs": "ADC isoles, squishies hors de vision",
        "tips": ["Paranoia (R) : coupe la vision globale + dash depuis n'importe ou.", "Shroud of Darkness (W) : spell shield. Active avant le burst ennemi.", "Dusk Trail (Q) : piste qui detecte les ennemis + DPS passif."],
    },

    "Nunu": {
        "role": "Jungle",
        "playstyle": "Clear rapide grace a consume, gank avec ball, R charge massif.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Conditioning | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"tank": {"ordre": ["Warmog's Armor", "Sunfire Aegis", "Thornmail", "Zeke's Convergence", "Gargoyle Stoneplate"], "chemins": {}, "note": "Warmog's + passive heal de Q = impossible a tuer."}},
        "counters": "Lee Sin, Graves, Rengar (duel early)",
        "strong_vs": "Champions a push rapide — Snowball engage devaste les lanes",
        "tips": ["Consume (Q) : mange les monstres pour heal massif.", "Biggest Snowball Ever (W) : roule + knock-up au bout. Charge en bush.", "Absolute Zero (R) : slow puis freeze AoE. Besoin de peel."],
    },

    "Olaf": {
        "role": "Jungle / Top Lane",
        "playstyle": "Berserk, ignore les cc avec R, niveau le plus fort du jeu level 2.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Spirit Visage", "Ravenous Hydra"], "chemins": {}, "note": "Ragnarok (R) ignore TOUS les cc. Engage frontalement sans risque."}},
        "counters": "Rammus (thornmail), Kha'Zix (kite), Graves",
        "strong_vs": "Champions cc-dependants — ton R les rend inutiles",
        "tips": ["Ragnarok (R) : invincible aux cc. Engage en R et ne t'arrete pas.", "Undertow (Q) : slow + reprends la hache pour reset le CD.", "Vicious Strikes (W) : AS + heal. Actif dans chaque trade."],
    },

    "Pantheon": {
        "role": "Top Lane / Mid Lane / Support",
        "playstyle": "Bully agressif early, global avec R. Snowball fort.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"lethality": {"ordre": ["Eclipse", "Serylda's Grudge", "Black Cleaver", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Eclipse + Q (Comet Spear) = poke enorme. Snowball et roam."}},
        "counters": "Darius, Malphite (R counter ton engage), Fiora (E block ton E)",
        "strong_vs": "Champions fragiles early — Spear Shot (Q) poke enorme",
        "tips": ["Aegis Assault (E) : direction face au damage. Bloque les projectiles.", "Grand Starfall (R) : global, atterrit partout. Roam apres push.", "Mortal Will (passif) : 5 stacks = prochain sort ameliore."],
    },

    "Poppy": {
        "role": "Top Lane / Jungle / Support",
        "playstyle": "Tank, contre les dashes, colle les ennemis aux murs, R envoie loin.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Grasp of the Undying (Resolve)", "resolve": "Demolish | Bone Plating | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"tank": {"ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate"], "chemins": {}, "note": "Keeper's Verdict (R) envoie l'ennemi loin — utilise pour peel ou engage."}},
        "counters": "Darius, Renekton (early bully)", "strong_vs": "Champions dash-dependants — Steadfast Presence (W) annule les dashes",
        "tips": ["Steadfast Presence (W) : annule tous les dashes dans la zone.", "Keeper's Verdict (R) : charge longue = envoie loin. Utilise pour le carry ennemi.", "Heroic Charge (E) : colle l'ennemi contre un mur = stun bonus."],
    },

    "Qiyana": {
        "role": "Mid Lane / Jungle",
        "playstyle": "Assassin, burst avec elements, R devastateur sur le terrain.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter", "secondary_tree": "Precision", "secondary": "Triumph | Last Stand"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Shadowflame"], "chemins": {}, "note": "Q sur herbe (slow) = poke constant avant burst."}},
        "counters": "Lissandra (cc), Galio, Malzahar",
        "strong_vs": "Orianna, Syndra, Yone (burst before they react)",
        "tips": ["Q sur herbe = slow, Q sur riviere = stun, Q sur mur = invisibilite.", "Supreme Display of Talent (R) : onde de choc vers un mur = AoE stun.", "Combo : dash E → Q herbe → R vers mur → burst."],
    },

    "Quinn": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Range top, extreme mobilite avec R (Valor), split push rapide.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Cut Down", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Kraken Slayer", "Lord Dominik's Regards", "Guardian Angel", "The Collector"], "chemins": {}, "note": "Passive Harrier (Q) blind = neutralise les auto-attackers."}},
        "counters": "Darius, Renekton (si tu approches)", "strong_vs": "Melee champions — blind neutralise leurs autos",
        "tips": ["Blinding Assault (Q) : marque + blind. Poke safe.", "Behind Enemy Lines (R) : vitesse extreme. Roam partout.", "Tag Team (R) : bascule entre Quinn et Valor mid-combat."],
    },

    "Rek'Sai": {
        "role": "Jungle",
        "playstyle": "Mobilite via tunnels, gank unpredictible, tanky fighter.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Sterak's Gage", "Black Cleaver", "Death's Dance", "Spirit Visage"], "chemins": {}, "note": "Tunnels = mobilite globale. Engage par surprise depuis n'importe ou."}},
        "counters": "Lee Sin, Graves, Xin Zhao",
        "strong_vs": "Champions immobiles — tunnels rendent tes ganks impredictibles",
        "tips": ["Burrow (W) : creuse des tunnels permanents partout sur la map.", "Prey Seeker (Q burrow) : detecte les ennemis au-dessus.", "Void Rush (R) : dash long depuis un tunnel."],
    },

    "Rell": {
        "role": "Support",
        "playstyle": "Engage tank, magnetise les ennemis, cc massif.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Bone Plating | Unflinching", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {"tank engage": {"ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate"], "chemins": {}, "note": "Full tank — ton R + Locket shield toute l'equipe en engage."}},
        "counters": "Soraka (heal efface tes degats), Lulu",
        "strong_vs": "Enchanteurs sans mobilite (Sona, Soraka)",
        "tips": ["Ferromancy (W) : dismount = AoE knock-up. Engage principal.", "Magnet Storm (R) : tire tous les ennemis proches vers toi.", "Full Tilt (E) : dash vers un allie ou ennemi."],
    },

    "Renata Glasc": {
        "role": "Support",
        "playstyle": "Enchanteur, revive les allies avec W, ultime qui fait se battre les ennemis.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Summon Aery (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Resolve", "secondary": "Font of Life | Revitalize"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"enchanteur": {"ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Redemption", "Knight's Vow", "Ardent Censer"], "chemins": {}, "note": "Bailout (W) revive un allie qui se bat apres la mort."}},
        "counters": "Blitzcrank, Nautilus (engage violent)",
        "strong_vs": "Toute equipe — R Hostile Takeover fait s'entre-tuer les ennemis",
        "tips": ["Bailout (W) : place sur l'ADC avant l'engage. Il revit s'il fait un kill.", "Hostile Takeover (R) : les ennemis attaquent leurs propres allies.", "Jetpack (E) : propulse un allie vers une cible."],
    },

    "Riven": {
        "role": "Top Lane",
        "playstyle": "Fighter mobile, combo complexe, skill cap tres haut, devastatrice maîtrisee.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"bruiser": {"ordre": ["Eclipse", "Serylda's Grudge", "Black Cleaver", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Eclipse pour le shield passif. Q en combo d'animation cancel = DPS max."}},
        "counters": "Darius, Renekton, Malphite (R stoppe ton engage)",
        "strong_vs": "Champions sans mobilite — dash en permanence",
        "tips": ["Broken Wings (Q) : 3 dashes en combo. Cancel animation apres chaque Q.", "Wind Slash (R) : execute sous 75% HP. Plus ils sont bas, plus c'est fort.", "Valor (E) : shield court. Utile pour absorber les cc et burst."],
    },

    "Rumble": {
        "role": "Top Lane / Jungle",
        "playstyle": "AP fighter, zone de feu, ultime global devastateur en teamfight.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"AP": {"ordre": ["Liandry's Anguish", "Demonic Embrace", "Rylai's Crystal Scepter", "Zhonya's Hourglass", "Rabadon's Deathcap"], "chemins": {}, "note": "Liandry's + flamethrower (Q) = DoT massif sur tanks."}},
        "counters": "Darius (gap close + saigne), Renekton, Garen",
        "strong_vs": "Champions melee et tanks — flamethrower ecrase les melees",
        "tips": ["The Equalizer (R) : place dans un couloir etroit = personne ne passe.", "Flamespitter (Q) : maintiens dans la zone de feu = DPS massif.", "Danger Zone : entre 50-100 heat = degats bonus. Ne pas overheater."],
    },

    "Ryze": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Mage DPS, ultra mana-dependant, scale infiniment, portail equipe avec R.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP mana": {"ordre": ["Rod of Ages", "Tear of the Goddess → Seraph's Embrace", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Mana = AP avec Seraph's. Stack mana autant que possible."}},
        "counters": "Zed, Talon, Fizz (burst avant ton DPS)",
        "strong_vs": "Champions immobiles — spam Q sur la cible rootee",
        "tips": ["Realm Warp (R) : portail equipe. Utilise pour macro split push.", "Rune Prison (W) : root. Q apres root = Q revient plus vite.", "Overload (Q) : proc Spellflow = CD reduit sur Q."],
    },

    "Senna": {
        "role": "Support / ADC",
        "playstyle": "Support ADC hybride, range infinie, heal global avec R. Unique.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {"primary_keystone": "Glacial Augment (Inspiration)", "inspiration": "Perfect Timing | Biscuit Delivery | Cosmic Insight", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Gathering Storm"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"enchanteur": {"ordre": ["Shurelya's Battlesong", "Shadowflame", "Luden's Tempest", "Rabadon's Deathcap", "Infinity Edge"], "chemins": {}, "note": "Stack ames pour AD + range infinie. Heal + degats = hybride unique."}},
        "counters": "Blitzcrank, Nautilus (engage violent)", "strong_vs": "Poke supports — range longue te permet de harceler",
        "tips": ["Absolution (passif) : collecte les ames sur les minions tues par tes allies.", "Last Embrace (W) : root. Utilise pour peel ou setup kills.", "Dawning Shadow (R) : heal global + bouclier. Tres utile."],
    },

    "Seraphine": {
        "role": "Support / Mid Lane",
        "playstyle": "Poke, soins, cc AoE. Forte en equipe groupee.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Summon Aery (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"enchanteur": {"ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Ardent Censer", "Staff of Flowing Water", "Shadowflame"], "chemins": {}, "note": "Moonstone pour les soins passifs, Aery amplifie le poke."}},
        "counters": "Blitzcrank, Nautilus (engage brutal)",
        "strong_vs": "Soraka, Sona, Lux (poke range superieure)",
        "tips": ["Passif : chaque 3e sort est double. Alterne les sorts pour activer.", "Encore (R) : canalise sur l'axe le plus long — touche autant d'ennemis possible.", "Beat Drop (E) : root si la cible est deja ralentie."],
    },

    "Shaco": {
        "role": "Jungle",
        "playstyle": "Ganks surprise, traps, clone. Tres fort en lower elo.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Dark Harvest (Domination)", "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards"], "chemins": {}, "note": "Deceive (Q) + Duskblade invisibilite = one-shot garanti."}},
        "counters": "Lee Sin (ward + reveal), Graves, Xin Zhao",
        "strong_vs": "Champions seuls, ADC sans peel",
        "tips": ["Deceive (Q) : teleporte + invisibilite. Gank par derriere systematiquement.", "Jack in the Box (W) : place en bush avant d'engager pour le fear.", "Hallucinate (R) : clone aide en fight et en bait."],
    },

    "Shen": {
        "role": "Top Lane",
        "playstyle": "Tank global avec R, shield a distance, split push safe.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Grasp of the Undying (Resolve)", "resolve": "Demolish | Second Wind | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"tank": {"ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Spirit Visage", "Gargoyle Stoneplate"], "chemins": {}, "note": "Stand United (R) : dash global vers un allie + shield. Utilise sur le carry engage."}},
        "counters": "Darius, Renekton, Camille (bully early)", "strong_vs": "Champions sans mobilite — Twilight Assault (Q) sustain constant",
        "tips": ["Stand United (R) : dash vers l'allie en danger. Sauve des vies.", "Shadow Dash (E) : taunt. Force l'ennemi a t'attaquer.", "Ki Barrier (passif) : shield apres chaque sort. Weave pour du sustain."],
    },

    "Shyvana": {
        "role": "Jungle",
        "playstyle": "Dragon en late, clear rapide, force via la rage. Tank ou AP hybride.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"AP hybride": {"ordre": ["Nashor's Tooth", "Riftmaker", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Dragon AP = Fireball (E) one-shot. Transforme en dragon apres 100 rage."}},
        "counters": "Lee Sin, Graves, Kha'Zix (duel early)",
        "strong_vs": "Champions groupes — AoE en forme de dragon",
        "tips": ["Dragon's Descent (R) : transforme en dragon. Engage au milieu des ennemis.", "Burnout (W) : AoE feu. Reste actif en fight permanemment.", "Twin Bite (Q) : double auto. Proc items on-hit deux fois."],
    },

    "Singed": {
        "role": "Top Lane",
        "playstyle": "Proxy farm, kite permanent, impossible a kite. Niche mais efficace.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Resolve", "secondary": "Second Wind | Overgrowth"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"tank MS": {"ordre": ["Rylai's Crystal Scepter", "Demonic Embrace", "Warmog's Armor", "Cosmic Drive", "Force of Nature"], "chemins": {}, "note": "Rylai's slow + traîne de poison = impossible de fuir."}},
        "counters": "Darius (pull stoppe le kite), Renekton, Illaoi",
        "strong_vs": "Nasus, Dr. Mundo, champions qui te suivent",
        "tips": ["Ne jamais se retourner pour combattre — courir et laisser le poison faire.", "Proxy farm entre les tours ennemies pour les faire paniquer.", "Fling (E) : jette l'ennemi par-dessus — vers la tour ou vers tes allies."],
    },

    "Sion": {
        "role": "Top Lane",
        "playstyle": "Tank enorme, charges Q devastatrices, HP infinis, reviit avec la rage.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Grasp of the Undying (Resolve)", "resolve": "Demolish | Second Wind | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Magical Footwear | Biscuit Delivery"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"full tank": {"ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Frozen Heart", "Gargoyle Stoneplate"], "chemins": {}, "note": "HP infinis avec Heartsteel + kill passif (revit avec % HP tue en rage)."}},
        "counters": "Darius, Renekton, Camille (kite ta charge)",
        "strong_vs": "Immobiles — Decimating Smash (Q) charge = unstoppable",
        "tips": ["Decimating Smash (Q) : charge longue = enorme knock-up. Pre-vise.", "Unstoppable Onslaught (R) : charge infinie = engage global.", "Soul Furnace (W) : shield + HP max bonus a chaque minion kill."],
    },

    "Skarner": {
        "role": "Jungle",
        "playstyle": "Tank CC, pique les ennemis et les drague sur toute la map.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Aftershock (Resolve)", "resolve": "Font of Life | Conditioning | Overgrowth", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"tank": {"ordre": ["Heartsteel", "Sunfire Aegis", "Frozen Heart", "Thornmail", "Warmog's Armor"], "chemins": {}, "note": "Impale (R) : empale et drague l'ennemi. Amene l'ADC sous la tour."}},
        "counters": "Lee Sin, Graves, Xin Zhao",
        "strong_vs": "ADC, carries isoles — R les emmene sous la tour",
        "tips": ["Impale (R) : supprime et drague un ennemi. Amene-le vers tes allies.", "Crystal Spires : controle les spires = plus de mana et vitesse.", "Shattered Earth (Q) : poke + slow. Core du kit."],
    },

    "Smolder": {
        "role": "ADC (Bot Lane)",
        "playstyle": "ADC scale via les stacks Q, sort puissant a haut niveau de stacks.",
        "summoner_spells": "Flash + Heal",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Presence of Mind | Legend: Bloodline | Cut Down", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"standard": {"ordre": ["Trinity Force", "Kraken Slayer", "Guinsoo's Rageblade", "Lord Dominik's Regards", "Mortal Reminder"], "chemins": {}, "note": "Stack Q jusqu'a 225+ pour les explosions. Scale fort en late."}},
        "counters": "Draven (early), Caitlyn (range poke)",
        "strong_vs": "Champions immobiles — E snare facile a atterrir",
        "tips": ["Super Scorcher Breath (Q) : stack jusqu'a 225 pour le bonus feu.", "Achooo!!! (R) : grand AoE. Utilise sur les groupes.", "E snare : utilisez avant Q pour le setup."],
    },

    "Swain": {
        "role": "Support / Mid Lane",
        "playstyle": "Tank AP, drain permanent, AoE en forme de demon. Tres resilient.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"AP tank": {"ordre": ["Rod of Ages", "Rylai's Crystal Scepter", "Liandry's Anguish", "Rabadon's Deathcap", "Void Staff"], "chemins": {}, "note": "Demonflare (R) + Rod of Ages = sustain infini en fight."}},
        "counters": "Blitzcrank, Nautilus (engage avant pull)",
        "strong_vs": "Champions fragiles — Nevermove (E) pull + stun",
        "tips": ["Vision of Empire (W) : slow + drain ames. Stack avant le combat.", "Nevermove (E) : jette la main qui root et pull vers toi.", "Demonic Ascension (R) : drain AoE. Reste actif = heal permanent."],
    },

    "Sylas": {
        "role": "Mid Lane",
        "playstyle": "Vole les ultimes enemies. Tres fort contre les equipes aux R puissants.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"bruiser AP": {"ordre": ["Riftmaker", "Rod of Ages", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "Vole des R puissants. Plus leur R est fort, plus tu es fort."}},
        "counters": "Fizz (dodge chains), Zed, LeBlanc",
        "strong_vs": "Katarina, Gangplank, Orianna (leur R devient ton outil de carry)",
        "tips": ["Hijack (R) : vole R de l'ennemi le plus proche.", "Chain Lash (Q) : snare si tu touches avec les deux bouts.", "Petricite Burst (W) : AoE auto-attack. Heal important en fight."],
    },

    "Syndra": {
        "role": "Mid Lane",
        "playstyle": "Burst one-shot level 9 avec R. Domination de lane.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"burst": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"], "chemins": {}, "note": "R a pleines spheres one-shot ADC + mid en late."}},
        "counters": "Fizz (dodge tout), Kassadin (R a portee), Zed",
        "strong_vs": "Ahri, Viktor, Orianna (immobiles face a ton burst)",
        "tips": ["Scatter the Weak (E) : stun si une sphere est dans la trajectoire.", "R charge : plus tu as de spheres, plus R fait de degats.", "Combo : Q (sphere) → E (stun) → W → Q → R."],
    },

    "Taliyah": {
        "role": "Jungle / Mid Lane",
        "playstyle": "Mage, poke safe avec rocher, mur global, mobilite sur la carte.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Hailblade + Refillable Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Phase Rush sur proc de sort = speed pour escape ou kite."}},
        "counters": "Lee Sin, Graves, Kha'Zix",
        "strong_vs": "Champions immobiles — Q poke safe constant",
        "tips": ["Seismic Shove (W) : lance les ennemis. Combo avec E pour stun.", "Weaver's Wall (R) : mur gigantesque. Coupe la carte en deux.", "Worked Ground (passif) : deja vu = moins de pierres. Kite en permanence."],
    },

    "Taric": {
        "role": "Support",
        "playstyle": "Tank enchanteur, invincibilite avec R, fort en duo coordonne.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Summon Aery (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Resolve", "secondary": "Font of Life | Revitalize"},
        "skill_order": "R des que possible. W > Q > E.",
        "starting_items": "Relic Shield + 2x Health Potion",
        "build_paths": {"tank enchanteur": {"ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Knight's Vow", "Warmog's Armor", "Gargoyle Stoneplate"], "chemins": {}, "note": "Cosmic Radiance (R) rend toute l'equipe invincible 2.5s."}},
        "counters": "Blitzcrank, Thresh (hook avant engage)",
        "strong_vs": "Toute equipe burst — R annule les degats",
        "tips": ["Cosmic Radiance (R) : 2.5s d'invincibilite — timing crucial.", "Bastion (W) : lie toi a un allie. Vos sorts se copient sur lui.", "Passive Bravado : tes sorts reset l'auto pour stun rapide."],
    },

    "Teemo": {
        "role": "Top Lane",
        "playstyle": "Kite, poison, champignons = vision et degats passifs. Annoying.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + Health Potion",
        "build_paths": {"AP on-hit": {"ordre": ["Nashor's Tooth", "Rabadon's Deathcap", "Shadowflame", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Nashor's + poison AP = DPS passif enorme."}},
        "counters": "Renekton (burst), Garen (E cleanse blind), Darius",
        "strong_vs": "Nasus, Jax, Tryndamere (Blinding Dart neutralise leur kit)",
        "tips": ["Blinding Dart (Q) : blind = neutralise les auto-attackers.", "Place champignons (R) en bush et en jungle pour vision + degats.", "Move Quick (W) : MS passif — actif pour sprint."],
    },

    "Trundle": {
        "role": "Jungle / Top Lane",
        "playstyle": "Vole l'armure et MR aux tanks, colonne, regeneration. Counter des tanks.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"tank": {"ordre": ["Trinity Force", "Sterak's Gage", "Sunfire Aegis", "Spirit Visage", "Frozen Heart"], "chemins": {}, "note": "Subjugate (R) vole les resistances du tank — il devient fragile, toi fort."}},
        "counters": "Lee Sin, Graves, Kha'Zix (duel early)",
        "strong_vs": "Tous les tanks — Subjugate (R) vole 40% de leur armure/MR",
        "tips": ["Subjugate (R) : ultime sur le tank ennemi — ses resistances te vont.", "Pillar of Ice (E) : coupe les fuites. Essential pour les ganks.", "Chomp (Q) : reduit l'AD ennemi temporairement. Core en trade."],
    },

    "Udyr": {
        "role": "Jungle",
        "playstyle": "Clear ultra-rapide, un des meilleurs junglers par statistiques.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Second Wind | Overgrowth"},
        "skill_order": "Wingborne Storm (R) > Blazing Stampede (R). Alterne les formes.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser tank": {"ordre": ["Sunfire Aegis", "Heartsteel", "Warmog's Armor", "Thornmail", "Gargoyle Stoneplate"], "chemins": {}, "note": "Sunfire + clear rapide = objectifs tres vite."}},
        "counters": "Lee Sin (duel), Kha'Zix, Rek'Sai",
        "strong_vs": "ADC, champions sans gap close",
        "tips": ["Alterne les formes pour les cooldowns reduits.", "Wingborne Storm (R glacier) : AoE slow = meilleur pour les teamfights.", "Blazing Stampede (R feu) : dash + fear = engage/escape."],
    },

    "Vel'Koz": {
        "role": "Support / Mid Lane",
        "playstyle": "Poke ultra-longue portee, true damage avec R, disintegration de la cible.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Lifeform Disintegration Ray (R) = true damage si 2 sorts ont touche."}},
        "counters": "Blitzcrank, Nautilus (engage ferme ton R)",
        "strong_vs": "Champions immobiles — 3 sorts = explosion de plasma true damage",
        "tips": ["Plasma Fission (Q) : divise en deux. Touche l'ennemi ET le split.", "Void Rift (W) : lente explosion. AoE utile en zone.", "LIFEFORM DISINTEGRATION RAY (R) : true damage. Reste immobile."],
    },

    "Vladimir": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Drain AP, invincible avec W (pool), scale tres fort, teamfight AoE.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Phase Rush (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"AP": {"ordre": ["Riftmaker", "Cosmic Drive", "Rabadon's Deathcap", "Shadowflame", "Void Staff"], "chemins": {}, "note": "Riftmaker true damage + drain (Q) = immortel en late."}},
        "counters": "Darius, Renekton, Garen (bully early avant pool CD)",
        "strong_vs": "Champions sans gap close — pool evite tout leur damage",
        "tips": ["Sanguine Pool (W) : invincible + slow AoE. Dodge les ultimes.", "Hemoplague (R) : amplifie tous les degats. Lance avant le burst equipe.", "Transfusion (Q) : heal sur kill. Spam pour sustain en lane."],
    },

    "Warwick": {
        "role": "Jungle / Top Lane",
        "playstyle": "Tank berserk, hound les ennemis a faible HP, suppress avec R.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Sterak's Gage", "Spirit Visage", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Infinite Duress (R) : suppress + fixe l'ennemi. Puis combo complet."}},
        "counters": "Kha'Zix, Graves, Rammus (counter engaging)",
        "strong_vs": "ADC, squishies a faible HP — Blood Hunt les detecte",
        "tips": ["Blood Hunt (passif) : detecte les ennemis sous 50% HP. Poursuis.", "Infinite Duress (R) : supprime en fixant. Combo apres.", "Jaws of the Beast (Q) : teleporte derriere si maintenu."],
    },

    "Wukong": {
        "role": "Top Lane / Jungle",
        "playstyle": "Engage, duplique, resistance passive. R double = cc permanent.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Sterak's Gage", "Black Cleaver", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Trinity Force + Crushing Blow (Q) = burst + armor shred rapide."}},
        "counters": "Darius, Renekton, Camille",
        "strong_vs": "Nasus, Malphite, Cho'Gath",
        "tips": ["Warrior Trickster (W) : clone + invisibilite. Fakes l'ennemi.", "Cyclone (R) peut etre caste deux fois — double knock-up.", "Stone Skin (passif) : armure bonus quand un ennemi est proche."],
    },

    "Xerath": {
        "role": "Support / Mid Lane",
        "playstyle": "Poke ultra longue portee, immobile mais devastateur a distance.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Rite of the Arcane (R) = 3-5 orbes depuis partout sur la map."}},
        "counters": "Blitzcrank, Nautilus (engage ferme ton kit immobile)",
        "strong_vs": "Champions immobiles — poke en dehors de ta portee",
        "tips": ["Arcanopulse (Q) : charge longue = plus de portee.", "Eye of Destruction (W) : slow au centre. AoE utile.", "Rite of the Arcane (R) : orbes partout sur la map. Finisher global."],
    },

    "Xin Zhao": {
        "role": "Jungle",
        "playstyle": "Engage brutal, knock-up, resistance avec R. Simple et efficace.",
        "summoner_spells": "Flash + Smite",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Resolve", "secondary": "Bone Plating | Unflinching"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Emberknife + Refillable Potion",
        "build_paths": {"bruiser": {"ordre": ["Trinity Force", "Sterak's Gage", "Black Cleaver", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Trinity Force + Q = burst + sustain fight."}},
        "counters": "Rammus (counter engage), Lee Sin, Graves",
        "strong_vs": "ADC, mid sans gap close, champions immobiles",
        "tips": ["Audacious Charge (E) : dash + slow. Always-on engage.", "Crescent Guard (Q) : 3e attaque = knock-up. Weave avec des autos.", "Crescent Sweep (R) : repousse tout sauf ceux dans le cone."],
    },

    "Yone": {
        "role": "Mid Lane / Top Lane",
        "playstyle": "Assassin fighter, deux ames, dash global avec R. Tres fort en duel.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Lethal Tempo (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {"hybride crit": {"ordre": ["Kraken Slayer", "Guinsoo's Rageblade", "Wit's End", "Sterak's Gage", "Death's Dance"], "chemins": {}, "note": "Hybride physique + magique. Rageblade amplifie les deux types."}},
        "counters": "Lissandra (root annule R), Malphite (R stoppe ton engage)",
        "strong_vs": "Ahri, Orianna, Syndra (dive et one-shot)",
        "tips": ["Mortal Steel (Q) : 3e Q = knock-up et dash. Weave dans les autos.", "Soul Unbound (E) : separe ton ame. Retour a ta position apres.", "Fate Sealed (R) : dash global qui pull tout le monde vers toi."],
    },

    "Yorick": {
        "role": "Top Lane",
        "playstyle": "Split push n°1 du jeu. Invoque des goules et la Maiden. Tour killer.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Tenacity | Last Stand", "secondary_tree": "Resolve", "secondary": "Demolish | Overgrowth"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {"split push": {"ordre": ["Trinity Force", "Sterak's Gage", "Sundered Sky", "Death's Dance", "Spirit Visage"], "chemins": {}, "note": "Trinity Force spike. Split push avec la Maiden — tours tombent vite."}},
        "counters": "Darius, Renekton, Camille (early bully)",
        "strong_vs": "Nasus, Malphite, Cho'Gath (ton split push force leur retour)",
        "tips": ["Last Rites (Q) : reset si tu tues avec. Farm et stack les goules.", "Eulogy of the Isles (R) : invoque la Maiden. Envoie-la split push solo.", "Dark Procession (W) : cage. Emprisonne l'ennemi dedans + goules le focus."],
    },

    "Yuumi": {
        "role": "Support",
        "playstyle": "S'attache aux allies, soins, acceleration. Invincible quand attachee.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {"primary_keystone": "Summon Aery (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Resolve", "secondary": "Font of Life | Revitalize"},
        "skill_order": "R des que possible. E > Q > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"enchanteur": {"ordre": ["Moonstone Renewer", "Shurelya's Battlesong", "Ardent Censer", "Staff of Flowing Water", "Redemption"], "chemins": {}, "note": "Reste attachee a l'ADC en permanence. Heal et amplifie ses degats."}},
        "counters": "Blitzcrank, Thresh (hook sans attachement)",
        "strong_vs": "Toute equipe — tu es intouchable quand attachee",
        "tips": ["Reste TOUJOURS attachee a un allie. Tu es invincible ainsi.", "Zoomies (E) : heal + AS. Priorite pendant les fights.", "Final Chapter (R) : cc en chaine. Lance quand l'ennemi est immobile."],
    },

    "Ziggs": {
        "role": "Mid Lane / Support",
        "playstyle": "Poke de tour ultra longue portee, detruit les batiments avec W.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Mega Inferno Bomb (R) : global AoE. Lance depuis ta propre base."}},
        "counters": "Zed, Talon, Fizz (dive les pokes)",
        "strong_vs": "Champions immobiles en lane, equipes sans engage",
        "tips": ["Satchel Charge (W) : double saut ou repousse. Detruit les tours pres de 25% HP.", "Mega Inferno Bomb (R) : global. Utilise pour finisher partout.", "Bounce (passif) : reset si tu tues. Waveclear perpetuel."],
    },

    "Zoe": {
        "role": "Mid Lane",
        "playstyle": "Poke burst avec E, vole les sorts et actifs, impredictible.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"burst AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Sleepy Trouble Bubble (E) endort → Q amplifie = burst enorme."}},
        "counters": "Fizz, Akali, Zed (gap close apres ton E rate)",
        "strong_vs": "Champions immobiles — E sleep + Q = burst facilement",
        "tips": ["Paddle Star (Q) : rebondit = plus de degats en angle.", "Sleepy Trouble Bubble (E) : endort. Attend que la cible soit endormie pour Q.", "More Sparkles! (passif) : vole les Summoner Spells et actifs d'items."],
    },

    "Zyra": {
        "role": "Support / Mid Lane",
        "playstyle": "Plantes qui font des degats, zone de controle, R AoE knock-up.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Spellthief's Edge + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Plantes ameliorees par l'AP. Poke + zone control permanent."}},
        "counters": "Blitzcrank, Nautilus (engage ferme ton placement de plantes)",
        "strong_vs": "Champions immobiles — plantes punissent les statics",
        "tips": ["Deadly Spines (Q) ou Grasping Roots (E) sur une graine = plante amelioree.", "Stranglethorns (R) : knock-up AoE. Combo avec Grasping Roots.", "Graine (W) : place avant le combat pour avoir des plantes en stock."],
    },

    "Naafiri": {
        "role": "Mid Lane",
        "playstyle": "Assassin simple avec meute de dahkabs, engage en pack. Accessible.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Electrocute (Domination)", "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter", "secondary_tree": "Sorcery", "secondary": "Manaflow Band | Transcendence"},
        "skill_order": "R des que possible. Q > W > E.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"lethality": {"ordre": ["Duskblade of Draktharr", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards"], "chemins": {}, "note": "Q en poke + lethality = burst fort."}},
        "counters": "Lissandra, Galio, Malzahar",
        "strong_vs": "ADC isoles, supports",
        "tips": ["Pack Hunt (R) : engage + meute renforcee.", "Hounds' Pursuit (W) : root si deux dahkabs touchent.", "Mange des minions pour reconstituer les dahkabs."],
    },

    "Mel": {
        "role": "Mid Lane",
        "playstyle": "Mage recente, renvoie les sorts, poke safe, forte en teamfight.",
        "summoner_spells": "Flash + Ignite",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Scorch", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Reflex (passif) renvoie les sorts — punish les poke enemies."}},
        "counters": "Zed, Talon, Fizz (gap close avant ton kit)",
        "strong_vs": "Champions a projectiles — ton passif les renvoie",
        "tips": ["Reflex (passif) : renvoie automatiquement les projectiles ennemis.", "Combo : Q → E → R pour le burst full.", "Positionne-toi pour renvoyer les sorts vers les ennemis groupes."],
    },

    "Ambessa": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Fighter aggressif, multi-dash, tres forte en duel et en fight.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Conqueror (Precision)", "precision": "Triumph | Legend: Alacrity | Last Stand", "secondary_tree": "Domination", "secondary": "Taste of Blood | Treasure Hunter"},
        "skill_order": "R des que possible. Q > E > W.",
        "starting_items": "Long Sword + 2x Health Potion",
        "build_paths": {"bruiser": {"ordre": ["Sundered Sky", "Black Cleaver", "Sterak's Gage", "Death's Dance", "Guardian Angel"], "chemins": {}, "note": "Dashes multiples + burst AD = inarretable en fight one-vs-one."}},
        "counters": "Darius (saigne), Camille, Fiora",
        "strong_vs": "Champions sans mobilite — tu enchaînes les dashes",
        "tips": ["Enchaîne les dashes Q/E pour maximiser le DPS.", "R : execute sous un seuil HP — reserve pour finir.", "Ne t'arrete jamais — ta force vient de la mobilite constante."],
    },

    "Hwei": {
        "role": "Mid Lane",
        "playstyle": "Mage polyvalent, 10 sorts a maîtriser. Poke, cc, degats, utilite.",
        "summoner_spells": "Flash + Teleport",
        "runes": {"primary_keystone": "Arcane Comet (Sorcery)", "sorcery": "Manaflow Band | Transcendence | Gathering Storm", "secondary_tree": "Inspiration", "secondary": "Biscuit Delivery | Cosmic Insight"},
        "skill_order": "R des que possible. QQ > QE > WQ > EQ.",
        "starting_items": "Doran's Ring + 2x Health Potion",
        "build_paths": {"AP": {"ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"], "chemins": {}, "note": "Meme build que les autres mages. Le kit s'adapte a toutes les situations."}},
        "counters": "Fizz, Zed, Talon (assassins qui evitent ton kit)",
        "strong_vs": "Champions immobiles — tes sorts ont beaucoup de portee",
        "tips": ["QQ : boule de feu principale — degats core.", "WQ : cage — cc zone en teamfight.", "EQ : heal pour toi ou un allie.", "R : canalise enormous AoE — utilise derriere l'ennemi."],
    },

}




def builds_to_chunks() -> list[tuple[str, str]]:
    """Convertit BUILDS en (id, texte) pour ChromaDB."""
    result = []
    for champ, data in BUILDS.items():
        slug = champ.lower().replace(" ", "_").replace("'", "")

        # Chunk principal : résumé du champion
        main = [
            f"BUILD COMPLET — {champ} ({data['role']}) :",
            f"Playstyle : {data['playstyle']}",
            f"Summoner Spells : {data['summoner_spells']}",
            f"Runes keystone : {data['runes'].get('primary_keystone', '?')}",
        ]
        prec = data['runes'].get('precision') or data['runes'].get('domination') or data['runes'].get('resolve') or data['runes'].get('sorcery', '')
        if prec:
            main.append(f"Runes lignes : {prec}")
        sec = data['runes'].get('secondary_tree', '')
        sec2 = data['runes'].get('secondary', '')
        if sec:
            main.append(f"Arbre secondaire : {sec} — {sec2}")
        main.append(f"Ordre sorts : {data['skill_order']}")
        main.append(f"Items de départ : {data['starting_items']}")

        tips = data.get('tips', [])
        if tips:
            main.append("Tips : " + " | ".join(tips if isinstance(tips, list) else [tips]))

        result.append((f"build_main_{slug}", "\n".join(main)))

        # Chunks par variante de build
        for variant_name, variant in data.get("build_paths", {}).items():
            lines = [f"BUILD {champ} — variante '{variant_name}' :"]
            ordre = variant.get("ordre", [])
            if ordre:
                lines.append(f"Ordre des items : {' → '.join(ordre)}")
            premier = variant.get("premier_retour", "")
            if premier:
                lines.append(f"Premier retour : {premier}")
            note = variant.get("note", "")
            if note:
                lines.append(f"Note : {note}")
            chemins = variant.get("chemins", {})
            for item, chemin in chemins.items():
                lines.append(f"  • {item} : {chemin}")
            result.append((f"build_{slug}_{variant_name[:20].replace(' ', '_')}", "\n".join(lines)))

        # Chunk matchup spécifique si présent
        for key, val in data.items():
            if key.startswith("matchup_"):
                result.append((f"{key}_{slug}", f"MATCHUP {champ} — {key.replace('matchup_', '')} :\n{val}"))

        # Counters / strong_vs
        if data.get("counters"):
            result.append((f"counters_{slug}", f"Counters de {champ} : {data['counters']}"))
        if data.get("strong_vs"):
            result.append((f"strong_{slug}", f"{champ} est fort contre : {data['strong_vs']}"))

    return result
