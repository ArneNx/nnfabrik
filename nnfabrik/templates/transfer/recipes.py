from typing import Dict

from nnfabrik.main import *


class Recipe(dj.Lookup):
    definition = """
    transfer_step: int
    -> Model
    -> Model.proj(prev_model_fn='model_fn', prev_model_hash='model_hash')
    """

    @property
    def post_restr(self) -> str:
        """
        Specifies which restrictions should be applied after transfer, e.g. which part should be kept the same
        """
        return ""

    def add_entry(
        self, transfer_from: Dict = None, transfer_to: Dict = None, transfer_step=0
    ):
        """
        Insert a recipe into the table.
        Args:
            transfer_from: entry to be transferred from
            transfer_to: entry to be transferred to
            transfer_step: integer that defines which transfer step this is applied in

        Returns:

        """
        entry = dict(
            **{f"prev_{k}": v for k, v in transfer_from.items()}, **transfer_to,
        )
        entry["transfer_step"] = transfer_step
        self.insert1(entry)


@schema
class DatasetTransferRecipe(Recipe):
    definition = """
    transfer_step: int
    -> Dataset
    -> Dataset.proj(prev_dataset_fn='dataset_fn', prev_dataset_hash='dataset_hash')
    """

    @property
    def post_restr(self):
        """
        This restriction clause is used to make sure that aside from switching datasets,
        the utilized trainer is to remain the same.
        """
        return "trainer_fn = prev_trainer_fn"


@schema
class ModelTransferRecipe(Recipe):
    definition = """
    transfer_step: int
    -> Model
    -> Model.proj(prev_model_fn='model_fn', prev_model_hash='model_hash')
    """

    @property
    def post_restr(self):
        """
        This restriction clause is used to make sure that aside from switching models,
        the utilized trainer is to remain the same.
        """
        return "trainer_fn = prev_trainer_fn"


@schema
class TrainerTransferRecipe(Recipe):
    definition = """
    transfer_step: int
    -> Trainer
    -> Trainer.proj(prev_trainer_fn='trainer_fn', prev_trainer_hash='trainer_hash')
    """

    @property
    def post_restr(self):
        """
        This restriction clause is used to make sure that aside from switching trainers,
        the utilized model is to remain the same.
        """
        return 'model_fn = prev_model_fn'
