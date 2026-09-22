"""Integration tests for the Hello World Agent.

Tests run fully offline — all LLM calls are mocked.
"""
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


@pytest.fixture(autouse=True)
def _add_app_to_path(add_agent_to_path):
    """Ensure app/ is on sys.path for all tests in this module."""
    pass


@pytest.mark.asyncio
async def test_agent_responds_hello_world():
    """REQ-02: Any input message must produce a response containing 'Hello World'."""
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", AsyncMock(return_value={"messages": [MagicMock(content="Hello World")]})):
        response = await agent.invoke("Hi there", "test-context-1")

    assert response.status == "completed"
    assert "Hello World" in response.message


@pytest.mark.asyncio
async def test_agent_responds_hello_world_any_input():
    """REQ-01 + REQ-02: Agent accepts any message and always returns Hello World."""
    from agent import SampleAgent

    agent = SampleAgent()

    for user_msg in ["Hello", "What is 2+2?", "Tell me a joke"]:
        with patch.object(agent, "_invoke_with_fallback", AsyncMock(return_value={"messages": [MagicMock(content="Hello World")]})):
            response = await agent.invoke(user_msg, "test-context-2")

        assert response.status == "completed"
        assert "Hello World" in response.message


@pytest.mark.asyncio
async def test_agent_stream_yields_hello_world():
    """REQ-02: stream() yields a final chunk containing 'Hello World'."""
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", AsyncMock(return_value={"messages": [MagicMock(content="Hello World")]})):
        chunks = []
        async for chunk in agent.stream("Say something", "test-context-3"):
            chunks.append(chunk)

    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert "Hello World" in final["content"]


@pytest.mark.asyncio
async def test_m1_milestone_logged(caplog):
    """M1: Message received milestone is logged when a non-empty message arrives."""
    import logging
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", AsyncMock(return_value={"messages": [MagicMock(content="Hello World")]})):
        with caplog.at_level(logging.INFO, logger="agent"):
            await agent._run_agent("Hello", "test-context-4")

    assert any("M1.achieved" in r.message for r in caplog.records)


@pytest.mark.asyncio
async def test_m2_milestone_logged(caplog):
    """M2: Response delivered milestone is logged after Hello World is emitted."""
    import logging
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(agent, "_invoke_with_fallback", AsyncMock(return_value={"messages": [MagicMock(content="Hello World")]})):
        with caplog.at_level(logging.INFO, logger="agent"):
            await agent._run_agent("Hello", "test-context-5")

    assert any("M2.achieved" in r.message for r in caplog.records)


@pytest.mark.asyncio
async def test_agent_error_handling():
    """Agent returns a graceful response (not an unhandled exception) when LLM fails."""
    from agent import SampleAgent

    agent = SampleAgent()

    # stream() catches the exception and yields a completed chunk with an error message
    with patch.object(agent, "_invoke_with_fallback", AsyncMock(side_effect=Exception("LLM unavailable"))):
        response = await agent.invoke("Hello", "test-context-6")

    # The agent should not crash — it must return a meaningful message
    assert response.message
    assert len(response.message) > 0


def test_system_prompt_contains_hello_world(add_agent_to_path):
    """REQ-02: System prompt instructs agent to always respond with Hello World."""
    from agent import get_system_prompt

    prompt = get_system_prompt()
    assert "Hello World" in prompt


def test_agent_instantiation(add_agent_to_path):
    """REQ-01: Agent can be instantiated without errors."""
    from agent import SampleAgent
    a = SampleAgent()
    assert a is not None
