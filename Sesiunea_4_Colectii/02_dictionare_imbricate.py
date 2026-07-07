catalog = [
  {"nume": "Alex", "clasa": 9, "note": [9, 10, 8]},
  {"nume": "Bianca", "clasa": 10, "note":}
]
for elev in catalog:
    if elev["clasa"] == 9:
        print(f"{elev['nume']} are notele {elev['note']}")
