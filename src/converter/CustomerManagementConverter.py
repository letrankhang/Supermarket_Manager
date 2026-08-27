from typing import List, Optional, Tuple
from src.entities.customer import Customer
from src.entities.customer_tier import CustomerTier
from src.dtos.CustomerManagementDTO import CustomerDetailDTO, CustomerManagementDTO

class CustomerManagementConverter:
    @staticmethod
    def to_customer_detail_dto(customer: Customer, tier: Optional[CustomerTier]) -> CustomerDetailDTO:
        tier_name = "Chưa có"
        discount_percent = 0
        if tier:
            tier_name = tier.tier_name
            discount_percent = tier.discount_percent
        elif customer.tier:
            tier_name = customer.tier.tier_name
            discount_percent = customer.tier.discount_percent
            
        return CustomerDetailDTO(
            customer_id=customer.customer_id,
            phone=customer.phone,
            full_name=customer.full_name or "",
            dob=customer.dob,
            total_points=customer.total_points,
            total_spent=float(customer.total_spent or 0.0),
            tier_name=tier_name,
            discount_percent=discount_percent,
            created_at=customer.created_at
        )


    @classmethod
    def to_customer_management_dto(
        cls, 
        customers: List[Customer], 
        tiers: List[CustomerTier], 
        count: int, 
        tier_counts: List[Tuple[str, int]]
    ) -> CustomerManagementDTO:
        tier_map = {t.tier_id: t for t in tiers}
        
        detail_dtos = []
        for customer in customers:
            tier = tier_map.get(customer.tier_id)
            detail_dtos.append(cls.to_customer_detail_dto(customer, tier))
            
        tier_summary = {tier_name: c for tier_name, c in tier_counts}
            
        return CustomerManagementDTO(
            customers=detail_dtos,
            total_count=count,
            tier_summary=tier_summary
        )
