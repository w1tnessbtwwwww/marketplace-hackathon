from sqlalchemy import insert, select
from ..models.product import Product
from ..abstract.abc_repo import AbstractRepository


class ProductRepository(AbstractRepository):
    model = Product


    async def create_product_if_not_exists(self, **kwargs):
        query = (
            select(self.model)
            .where(self.model.articul == kwargs["articul"])
        )

        product = self._session.execute(query).scalars().first()

        if not product:
            result = self.create(**kwargs)
            await self.commit()
            return result.scalars().first()

        return product