from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class PostMetadata(BaseModel):
    post_id: str = Field(..., description="Reddit post ID")
    url: str = Field(..., description="URL to the Reddit post")
    created_utc: str = Field(..., description="Post creation timestamp")
    score: int = Field(..., description="Post score/upvotes")
    num_comments: int = Field(..., description="Number of comments")


class Classification(BaseModel):
    topic_category: str = Field(..., description="The main topic of the post (e.g., 'AI tools', 'Mental health').")
    post_type: str = Field(..., description="Type of the post (e.g., 'Question', 'Story', 'Rant', 'Opinion').")
    user_intent: str = Field(..., description="What the author is trying to do or solve.")

class EmotionAnalysis(BaseModel):
    primary_emotion: str = Field(..., description="Primary emotion of the post author.")
    emotion_strength: int = Field(..., description="Strength of the emotion (1-10).")
    comment_emotions: List[str] = Field(..., description="Dominant emotions found in comments.")
    emotional_clusters: List[str] = Field(..., description="Groups of emotions present in the discussion.")

class PainPoints(BaseModel):
    pain_points: List[str] = Field(..., description="List of specific struggles or problems mentioned by users.")
    pain_point_clusters: List[str] = Field(..., description="Grouped categories of pain points.")
    frequency: Dict[str, int] = Field(default_factory=dict, description="Estimated frequency of each pain point cluster.")

class Desires(BaseModel):
    explicit_desires: List[str] = Field(..., description="Direct 'I want' or 'I wish' statements.")
    implicit_desires: List[str] = Field(..., description="Desires implied by complaints or questions.")
    direction_of_desire: List[str] = Field(..., description="Qualities users want (e.g., 'speed', 'trust').")

class Opportunities(BaseModel):
    market_gaps: List[str] = Field(..., description="Problems with no current solution.")
    unmet_needs: List[str] = Field(..., description="Needs not fully satisfied by existing tools.")
    feature_requests: List[str] = Field(..., description="Specific features users are asking for.")
    manual_hacks: List[str] = Field(..., description="Workarounds users are using (automation opportunities).")

class UserArchetypes(BaseModel):
    user_types: List[str] = Field(..., description="Types of users identified (e.g., 'beginner', 'expert').")
    motivations: List[str] = Field(..., description="What drives these users (e.g., 'save time', 'gain status').")

class CommunityConsensus(BaseModel):
    recurring_advice: List[str] = Field(..., description="Advice that appears multiple times.")
    recurring_complaints: List[str] = Field(..., description="Complaints that appear multiple times.")
    myths_misunderstandings: List[str] = Field(..., description="Common misconceptions.")
    debates: List[str] = Field(..., description="Topics where users disagree.")
    community_norms: List[str] = Field(..., description="Unwritten rules or behaviors of the community.")

class Risks(BaseModel):
    fears: List[str] = Field(..., description="What users are afraid of.")
    doubts: List[str] = Field(..., description="Skepticism expressed by users.")
    risk_perceptions: List[str] = Field(..., description="Perceived dangers or downsides.")

class FinalSummary(BaseModel):
    post_metadata: PostMetadata
    classification: Classification
    emotion_analysis: EmotionAnalysis
    pain_points: PainPoints
    desires: Desires
    opportunities: Opportunities
    user_archetypes: UserArchetypes
    community_consensus: CommunityConsensus
    risks: Risks
    high_level_summary: str = Field(..., description="A human-readable high-level summary of the analysis.")
