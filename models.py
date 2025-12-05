from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class PostMetadata(BaseModel):
    post_id: str = Field(..., description="Reddit post ID")
    url: str = Field(..., description="URL to the Reddit post")
    created_utc: str = Field(..., description="Post creation timestamp")
    score: int = Field(..., description="Post score/upvotes")
    num_comments: int = Field(..., description="Number of comments")
    subreddit: str = Field(..., description="Subreddit name")
    post_age_days: int = Field(default=0, description="Age of post in days")

class Classification(BaseModel):
    topic_category: str = Field(..., description="The main topic of the post")
    post_type: str = Field(..., description="Type of the post (e.g., 'Question', 'News Article', 'Discussion')")
    user_intent: str = Field(..., description="What the author is trying to do or solve")
    confidence: float = Field(..., description="Confidence score 0-1 for classification accuracy")

class EmotionAnalysis(BaseModel):
    primary_emotion: str = Field(..., description="Primary emotion of the post author")
    emotion_strength: int = Field(..., description="Strength of the emotion (1-10)")
    comment_emotions: List[str] = Field(..., description="Dominant emotions found in comments")
    emotional_clusters: List[str] = Field(..., description="Groups of emotions present in the discussion")
    emotion_confidence: float = Field(..., description="Confidence in emotion detection 0-1")

class PainPoints(BaseModel):
    pain_points: List[str] = Field(..., description="List of specific struggles or problems mentioned")
    pain_point_clusters: List[str] = Field(..., description="Grouped categories of pain points")
    frequency: Dict[str, int] = Field(default_factory=dict, description="Frequency of each pain point cluster")
    pain_sentences: List[str] = Field(..., description="Exact sentences expressing pain from comments")

class Triggers(BaseModel):
    root_causes: List[str] = Field(..., description="Underlying root causes of the pain points")
    system_limitations: List[str] = Field(..., description="System or tool limitations causing problems")
    environmental_factors: List[str] = Field(..., description="External factors contributing to issues")
    emotional_drivers: List[str] = Field(..., description="Emotional factors driving the pain")

class Desires(BaseModel):
    explicit_desires: List[str] = Field(..., description="Direct 'I want' or 'I wish' statements")
    implicit_desires: List[str] = Field(..., description="Desires implied by complaints or questions")
    direction_of_desire: List[str] = Field(..., description="Qualities users want (e.g., 'speed', 'trust')")
    desire_sentences: List[str] = Field(..., description="Exact sentences expressing desires from comments")

class Behaviors(BaseModel):
    current_tools: List[str] = Field(..., description="Tools or methods currently being used")
    workarounds: List[str] = Field(..., description="Manual hacks or workarounds users employ")
    failed_attempts: List[str] = Field(..., description="Things users tried that didn't work")
    search_patterns: List[str] = Field(..., description="Common search queries or questions asked")
    behavior_intent: str = Field(..., description="Overall intent behind user behaviors")

class Keywords(BaseModel):
    high_frequency_phrases: List[str] = Field(..., description="Most commonly used phrases")
    pain_phrases: List[str] = Field(..., description="Phrases expressing pain or frustration")
    desire_phrases: List[str] = Field(..., description="Phrases expressing wants or needs")
    topic_keywords: List[str] = Field(..., description="Key topic-related keywords")

class Opportunities(BaseModel):
    market_gaps: List[str] = Field(..., description="Problems with no current solution")
    unmet_needs: List[str] = Field(..., description="Needs not fully satisfied by existing tools")
    feature_requests: List[str] = Field(..., description="Specific features users are asking for")
    manual_hacks: List[str] = Field(..., description="Workarounds users are using (automation opportunities)")
    opportunity_context: str = Field(..., description="Context explaining the opportunity")

class UserArchetypes(BaseModel):
    user_types: List[str] = Field(..., description="Types of users identified")
    motivations: List[str] = Field(..., description="What drives these users")
    identity_indicators: List[str] = Field(..., description="Characteristics that identify user types")

class CommunityConsensus(BaseModel):
    recurring_advice: List[str] = Field(..., description="Advice that appears multiple times")
    recurring_complaints: List[str] = Field(..., description="Complaints that appear multiple times")
    myths_misunderstandings: List[str] = Field(..., description="Common misconceptions")
    debates: List[str] = Field(..., description="Topics where users disagree")
    community_norms: List[str] = Field(..., description="Unwritten rules or behaviors of the community")

class Risks(BaseModel):
    fears: List[str] = Field(..., description="What users are afraid of")
    doubts: List[str] = Field(..., description="Skepticism expressed by users")
    risk_perceptions: List[str] = Field(..., description="Perceived dangers or downsides")
    edge_cases: List[str] = Field(..., description="Unusual or extreme scenarios mentioned")

class TopicConflict(BaseModel):
    topic: str = Field(..., description="The topic of conflict")
    positions: List[str] = Field(..., description="Different positions on the topic")

class Contradictions(BaseModel):
    topic_conflicts: List[TopicConflict] = Field(..., description="Conflicting viewpoints on topics")

class OpportunityScore(BaseModel):
    pain_intensity: int = Field(..., description="How intense is the pain? (1-10)")
    pain_frequency: int = Field(..., description="How often does this pain occur? (1-10)")
    market_size: int = Field(..., description="How many people have this problem? (1-10)")
    competition_gap: int = Field(..., description="How underserved is this market? (1-10)")
    desire_strength: int = Field(..., description="How badly do users want a solution? (1-10)")
    workaround_effort: int = Field(..., description="How much effort do workarounds require? (1-10)")
    spending_signals: int = Field(..., description="Evidence of willingness to pay (1-10)")
    final_score: int = Field(..., description="Total opportunity score (sum of above)")

class Context(BaseModel):
    sarcasm_flags: List[str] = Field(default_factory=list, description="Comments that may be sarcastic")
    political_context: bool = Field(default=False, description="Is there political context?")
    external_references: List[str] = Field(default_factory=list, description="External links or references")
    sensitivity_level: int = Field(default=0, description="Sensitivity level 0-10")

class SourceEvaluation(BaseModel):
    credibility_score: float = Field(default=0.0, description="Source credibility 0-1")
    bias_indicators: List[str] = Field(default_factory=list, description="Potential biases detected")
    fact_check_required: bool = Field(default=False, description="Does this need fact-checking?")

class ActionSignals(BaseModel):
    willingness_to_pay: List[str] = Field(default_factory=list, description="Signals of payment intent")
    requests_for_tools: List[str] = Field(default_factory=list, description="Direct tool requests")
    calls_for_action: List[str] = Field(default_factory=list, description="Calls to action")
    solution_search_intent: List[str] = Field(default_factory=list, description="Active solution seeking")

class FinalSummary(BaseModel):
    post_metadata: PostMetadata
    classification: Classification
    emotion_analysis: EmotionAnalysis
    pain_points: PainPoints
    triggers: Triggers
    desires: Desires
    behaviors: Behaviors
    keywords: Keywords
    opportunities: Opportunities
    user_archetypes: UserArchetypes
    community_consensus: CommunityConsensus
    risks: Risks
    contradictions: Contradictions
    opportunity_score: OpportunityScore
    context: Context
    source_evaluation: SourceEvaluation
    action_signals: ActionSignals
    high_level_summary: str = Field(..., description="A comprehensive high-level summary of the analysis")
