# conda activate my_rdkit_env
# python pyscript.py
# ----------------------------------------------------------------
#            bash Miniconda3-latest-Linux-x86_64.sh or bash Miniconda3-latest-Linux-x86_64.sh -b
#            /miniconda3/bin/conda init
#            conda activate
#            conda create --name my_rdkit_env python=3.9 -y 
#            conda install -c conda-forge rdkit -y
#            conda install -c anaconda pymongo -y

# ----------------------------------------------------------------

# To update a property of db collection
# from rdkit import Chem
# import pymongo
# from pymongo import MongoClient  # For MongoDB connection

# # Connect to MongoDB
# client = MongoClient("mongodb://covaln:Cov%40ln@192.168.22.20:27017/?authSource=admin") 
# db = client["test"] 
# collection = db["testPDB"] 

# # Fetch all records with an SDF structure
# documents = collection.find({"SDF_STRUCTURE": {"$exists": True}})

# bulk_updates = []

# for doc in documents:
#     sdf_data = doc.get("SDF_STRUCTURE")  # Safely get SDF_STRUCTURE

#     if not sdf_data:  # If sdf_data is None or empty
#         pdb_data = None  # Set PDB_DATA to None
#     else:
#         # Convert SDF data to PDB
#         mol = Chem.MolFromMolBlock(sdf_data)
#         if mol:
#             # Set residue info for proper PDB formatting
#             residue_name = "MOL"
#             atom_index = 1  # Start from 1 for atoms
            
#             for atom in mol.GetAtoms():
#                 atom_name = f"{atom.GetSymbol()}{atom_index}"
#                 info = Chem.AtomPDBResidueInfo(atomName=f'{atom_name:<4}', 
#                                                residueName=residue_name,
#                                                residueNumber=1)
#                 atom.SetMonomerInfo(info)
#                 atom_index += 1

#             pdb_data = Chem.MolToPDBBlock(mol)
#         else:
#             pdb_data = None  # If molecule conversion fails, set to None

#     # Prepare update query
#     bulk_updates.append({
#         "filter": {"_id": doc["_id"]},  # Match document by unique ID
#         "update": {"$set": {"PDB_DATA": pdb_data}}
#     })

# # Perform bulk update
# if bulk_updates:
#     collection.bulk_write([pymongo.UpdateOne(update["filter"], update["update"]) for update in bulk_updates])

# print(f"Updated {len(bulk_updates)} documents with PDB_DATA.")
# ----------------------------------------------------------------

# # to remove a property from a db collection

# import pymongo  # <-- Add this import
# from pymongo import MongoClient  # For MongoDB connection

# # Connect to MongoDB
# client = MongoClient("mongodb://covaln:Cov%40ln@192.168.22.20:27017/?authSource=admin") 
# db = client["test"] 
# collection = db["testPDB"] 

# # Fetch all documents that contain the "PDB_DATA" field
# documents = collection.find({"PDB_DATA": {"$exists": True}})

# bulk_updates = []

# for doc in documents:
#     # Prepare delete update
#     bulk_updates.append({
#         "filter": {"_id": doc["_id"]},  # Match document by unique ID
#         "update": {"$unset": {"PDB_DATA": ""}}  # Remove PDB_DATA field
#     })

# # Perform bulk update
# if bulk_updates:
#     collection.bulk_write([pymongo.UpdateOne(update["filter"], update["update"]) for update in bulk_updates])

# print(f"Removed PDB_DATA from {len(bulk_updates)} documents.")

from rdkit import Chem
import pymongo
from pymongo import MongoClient  # For MongoDB connection

# Connect to MongoDB
client = MongoClient("mongodb://covaln:Cov%40ln@192.168.22.20:27017/?authSource=admin") 
db = client["test"] 
collection = db["drugs"] 

# Fetch all records with an SDF structure
documents = collection.find({"SDF_STRUCTURE": {"$exists": True}})

bulk_updates = []

for doc in documents:
    sdf_data = doc.get("SDF_STRUCTURE")  # Safely get SDF_STRUCTURE

    if not sdf_data:  # If sdf_data is None or empty
        pdb_data = None  # Set PDB_DATA to None
    else:
        # Convert SDF data to PDB
        mol = Chem.MolFromMolBlock(sdf_data)
        if mol:
            # Set residue info for proper PDB formatting
            residue_name = "MOL"
            atom_index = 1  # Start from 1 for atoms
            
            for atom in mol.GetAtoms():
                atom_name = f"{atom.GetSymbol()}{atom_index}"
                info = Chem.AtomPDBResidueInfo(atomName=f'{atom_name:<4}', 
                                               residueName=residue_name,
                                               residueNumber=1)
                atom.SetMonomerInfo(info)
                atom_index += 1

            pdb_data = Chem.MolToPDBBlock(mol)
        else:
            pdb_data = None  # If molecule conversion fails, set to None

    # Prepare update query
    bulk_updates.append({
        "filter": {"_id": doc["_id"]},  # Match document by unique ID
        "update": {"$set": {"PDB_DATA": pdb_data}}
    })

# Perform bulk update
if bulk_updates:
    collection.bulk_write([pymongo.UpdateOne(update["filter"], update["update"]) for update in bulk_updates])

print(f"Updated {len(bulk_updates)} documents with PDB_DATA.")
