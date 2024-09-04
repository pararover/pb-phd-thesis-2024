obs_edges_keV = [0.42, 0.55, 0.72, 0.88]
epsilon = 0.02
edge_df = identify_edges(edgedf_keV, (energy_lo, energy_hi), elements, obs_edges_keV, epsilon=epsilon)
temp_df = edge_df.drop(axis='index', index=3)