rule Hex_Rich
{
	strings:
		$rich_1 = { 52 69 63 68 5e 87 97 1f }
		$rich_2 = { 52 69 63 68 2a b4 da 42 }
		$rich_3 = { 52 69 63 68 a4 49 7f ba }
		$rich_4 = { 52 69 63 68 35 b3 8a d4 }
		$rich_5 = { 52 69 63 68 a9 e7 d4 6d }
		$rich_6 = { 52 69 63 68 fb 0f ab d8 }
		$rich_7 = { 52 69 63 68 bc 84 08 41 }
		$rich_8 = { 52 69 63 68 2a b4 5a 42 }
		$rich_9 = { 52 69 63 68 fd 0f ab 98 }
		$rich_10 = { 52 69 63 68 9a 7a 93 cd }
		$rich_11 = { 52 69 63 68 39 38 3d 81 }
		$rich_12 = { 52 69 63 68 7a 82 00 97 }
		$rich_13 = { 52 69 63 68 18 18 83 8a }
		$rich_14 = { 52 69 63 68 fb 0f ab b8 }
		$rich_15 = { 52 69 63 68 de 86 97 1f }
		$rich_16 = { 52 69 63 68 25 c8 d6 a5 }
		$rich_17 = { 52 69 63 68 96 71 d5 94 }
		$rich_18 = { 52 69 63 68 bb d1 65 21 }
		$rich_19 = { 52 69 63 68 bf ba d8 b5 }
		$rich_20 = { 52 69 63 68 67 26 94 d2 }
		$rich_21 = { 52 69 63 68 f6 8d a9 a4 }
		$rich_22 = { 52 69 63 68 ab 38 fe d1 }

	condition:
		any of them 
}