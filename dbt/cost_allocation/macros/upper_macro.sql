{% macro upper_case(date_column) %}
    upper({{ date_column }})
{% endmacro %}